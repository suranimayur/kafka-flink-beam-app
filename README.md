# Kafka Beam Application

## Project Summary

This project implements a data processing pipeline using Apache Beam that consumes messages from a Kafka topic, processes them to determine if the age derived from the date of birth is even or odd, and publishes the results to two separate Kafka topics. Additionally, it persists the processed messages to SQLite.

## Features

- **Kafka Integration**: Consumes messages from a Kafka topic and publishes to multiple topics
- **Data Processing**: Calculates age from date of birth and categorizes as even/odd
- **Data Persistence**: Stores processed messages in SQLite database
- **Error Handling**: Robust error handling and logging
- **Testing**: Comprehensive test suite for data processing logic

## Project Structure

```
kafka-beam-app/
│
├── README.md
├── setup.py
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

## Prerequisites

- Python 3.8 or higher
- Apache Kafka
- SQLite3

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/suranimayur/kafka-flink-beam-app.git
   cd kafka-flink-beam-app
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

## Usage

1. **Start Kafka**:
   Ensure Kafka is running with the following topics:
   - `inbound_topic`: For incoming messages
   - `even_topic`: For messages with even ages
   - `odd_topic`: For messages with odd ages
   - `error_topic`: For error messages

2. **Run the Application**:
   ```bash
   python -m app.main
   ```

3. **Send Test Messages**:
   Use the Kafka console producer to send test messages:
   ```bash
   kafka-console-producer --broker-list localhost:9092 --topic inbound_topic
   ```
   Example message format:
   ```json
   {"name": "John Doe", "date_of_birth": "1990-01-01"}
   ```

## Testing

Run the test suite:
```bash
pytest tests/
```

## Configuration

The application can be configured by modifying the following parameters in `app/main.py`:
- Kafka broker address
- Topic names
- SQLite database path

## Error Handling

The application includes comprehensive error handling:
- Invalid date formats
- Missing required fields
- Kafka connection issues
- Database errors

All errors are logged to both console and file (`logs/app.log`).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Mayur Surani - suranimayur@gmail.com

Project Link: [https://github.com/suranimayur/kafka-flink-beam-app](https://github.com/suranimayur/kafka-flink-beam-app) 