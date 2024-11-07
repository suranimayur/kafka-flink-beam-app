import logging
from data_processor import process_kafka_messages

def main():
    process_kafka_messages()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()