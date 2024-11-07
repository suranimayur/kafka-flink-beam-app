#### Project Title: Kafka Flink/Beam Application

**Overview:**
This project demonstrates a data processing application using Apache Kafka and Apache Flink/Beam. The application consumes messages from a Kafka topic containing user information (Name, Address, Date of Birth), processes the data to categorize users based on their age, and republishes the categorized data to two different Kafka topics while persisting the messages to a local datastore.

**Key Features:**
- Consume messages from a single Kafka topic.
- Determine if the age is even or odd and publish to appropriate Kafka topics (EVEN_TOPIC and ODD_TOPIC).
- Persist messages to a local file or database.
- Test the application with sample data.



kafka-flink-beam-app/
│
├── README.md               # Project summary and instructions
├── requirements.txt        # Python dependencies (if using Beam)
├── flink_app.py            # Main Flink application script
├── beam_app.py             # Main Beam application script
│
├── data/                   # Directory for storing data files
│   └── published_data.txt  # File for persisting published messages
│
├── tests/                  # Directory for tests
│   └── test_app.py         # Test cases for the application
│
└── .env                    # Environment variables (if needed)
```
