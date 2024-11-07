import json
import logging
from datetime import datetime
from confluent_kafka import Consumer, Producer # type: ignore


KAFKA_BROKER = 'localhost:9092'
INBOUND_TOPIC = 'inbound_topic'
EVEN_TOPIC = 'even_topic'
ODD_TOPIC = 'odd_topic'

def calculate_age(dob):
    birth_date = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def process_kafka_messages():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'my_group',
        'auto.offset.reset': 'earliest'
    })
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})

    consumer.subscribe([INBOUND_TOPIC])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Consumer error: {msg.error()}")
                continue
            
            data = json.loads(msg.value().decode('utf-8'))
            age = calculate_age(data['DateOfBirth'])
            if age % 2 == 0:
                producer.produce(EVEN_TOPIC, value=msg.value())
                logging.info(f"Published to EVEN_TOPIC: {data}")
            else:
                producer.produce(ODD_TOPIC, value=msg.value())
                logging.info(f"Published to ODD_TOPIC: {data}")
            
            producer.flush()

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()