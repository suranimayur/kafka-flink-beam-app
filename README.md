# Kafka Beam  Application

## Project Summary

This project implements a data processing pipeline using Apache Beam or Flink that consumes messages from a Kafka topic, processes them to determine if the age derived from the date of birth is even or odd, and publishes the results to two separate Kafka topics. Additionally, it persists the processed messages to a specified datastore (e.g., SQLite).

## Project Structure

```
kafka-beam-flink-app/
│
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data_processor.py
│   └── logger.py
└── tests/
    ├── __init__.py
    └── test_data_processor.py
```

## Goals

- Create a scalable data processing pipeline that reads from Kafka.
- Process user data to determine age and categorize it as even or odd.
- Publish processed data to separate Kafka topics.
- Implement unit tests for the processing logic.

## Technologies Used

- **Apache Beam**: For building the data processing pipeline.
- **Kafka**: For message brokering.
- **Python**: The programming language for implementation.
- **SQLAlchemy**: For data persistence.
- **Pipenv**: For managing project dependencies.

## Installation Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/suranimayur/kafka-beam-flink-app.git
   cd kafka-beam-flink-app
   ```

2. **Create a Virtual Environment Using Pipenv**:

   ```bash
   pip install pipenv
   pipenv shell
   ```

3. **Install Necessary Libraries**:

   Create a `requirements.txt` file with the following content:

   ```plaintext
   apache-beam[gcp]
   confluent-kafka
   pyspark
   sqlalchemy
   ```

   Then install the libraries:

   ```bash
   pipenv install -r requirements.txt
   ```

## Usage Instructions

1. **Start Zookeeper and Kafka**:

   Ensure that Zookeeper and Kafka are running:

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
   ```

2. **Create Kafka Topics**:

   ```bash
   bin/kafka-topics.sh --create --topic inbound_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   bin/kafka-topics.sh --create --topic even_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   bin/kafka-topics.sh --create --topic odd_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

3. **Produce Sample Data**:

   You can use the Kafka console producer to send sample data:

   ```bash
   bin/kafka-console-producer.sh --topic inbound_topic --bootstrap-server localhost:9092
   ```

   Sample input (JSON format):

   ```json
   {"Name": "John Doe", "Address": "123 Main St", "DateOfBirth": "1990-01-01"}
   ```

4. **Run the Application**:

   In a separate terminal, run your application:

   ```bash
   python app/main.py
   ```

5. **Consume from Topics**:

   To check the output in the even and odd topics, use:

   ```bash
   bin/kafka-console-consumer.sh --topic even_topic --bootstrap-server localhost:9092 --from-beginning
   bin/kafka-console-consumer.sh --topic odd_topic --bootstrap-server localhost:9092 --from-beginning
   ```

## Testing

Run the unit tests to ensure the processing logic works as expected:

```bash
python -m unittest discover tests/
```



This project is licensed under the MIT License.

---

