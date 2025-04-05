import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.kafka import ReadFromKafka, WriteToKafka
from apache_beam.io.jdbc import WriteToJdbc
import json
import logging
from datetime import datetime
from typing import Dict, Any
import sqlite3
from app.data_processor import process_message
from app.logger import setup_logger

logger = setup_logger(__name__)

class ProcessMessage(beam.DoFn):
    def process(self, element):
        try:
            # Parse the Kafka message
            message = json.loads(element[1].decode('utf-8'))
            
            # Process the message
            processed_data = process_message(message)
            
            # Determine the target topic based on age
            target_topic = 'even_topic' if processed_data['age'] % 2 == 0 else 'odd_topic'
            
            # Prepare the output message
            output_message = {
                'original_data': message,
                'processed_data': processed_data,
                'processing_timestamp': datetime.now().isoformat()
            }
            
            # Return the message with the target topic
            yield (target_topic.encode('utf-8'), json.dumps(output_message).encode('utf-8'))
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            yield ('error_topic'.encode('utf-8'), json.dumps({
                'error': str(e),
                'original_message': element[1].decode('utf-8')
            }).encode('utf-8'))

def run_pipeline():
    # Define pipeline options
    options = PipelineOptions(
        runner='DirectRunner',
        project='kafka-beam-app',
        temp_location='./temp',
        setup_file='./setup.py'
    )

    # Create the pipeline
    with beam.Pipeline(options=options) as p:
        # Read from Kafka
        messages = (p
            | 'ReadFromKafka' >> ReadFromKafka(
                consumer_config={
                    'bootstrap.servers': 'localhost:9092',
                    'group.id': 'beam-consumer'
                },
                topics=['inbound_topic']
            )
        )

        # Process messages
        processed = (messages
            | 'ProcessMessages' >> beam.ParDo(ProcessMessage())
        )

        # Write to Kafka topics
        _ = (processed
            | 'WriteToKafka' >> WriteToKafka(
                producer_config={
                    'bootstrap.servers': 'localhost:9092'
                }
            )
        )

        # Write to SQLite
        _ = (processed
            | 'FormatForSQLite' >> beam.Map(lambda x: (
                x[0].decode('utf-8'),  # topic
                x[1].decode('utf-8')   # message
            ))
            | 'WriteToSQLite' >> beam.Map(lambda x: write_to_sqlite(x))
        )

def write_to_sqlite(data):
    try:
        conn = sqlite3.connect('processed_messages.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert the data
        cursor.execute(
            'INSERT INTO processed_messages (topic, message) VALUES (?, ?)',
            (data[0], data[1])
        )
        
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Error writing to SQLite: {str(e)}")

if __name__ == '__main__':
    logger.info("Starting the pipeline...")
    run_pipeline()
    logger.info("Pipeline completed.") 