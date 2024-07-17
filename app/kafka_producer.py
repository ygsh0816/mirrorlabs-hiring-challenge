# app/kafka_producer.py
import json
import os

from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_message(message: dict):
    producer.send(KAFKA_TOPIC, value=message)
    producer.flush()
