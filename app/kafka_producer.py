# app/kafka_producer.py
from kafka import KafkaProducer
import json
from .config import KAFKA_BROKER_URL, KAFKA_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(message: dict):
    producer.send(KAFKA_TOPIC, value=message)
    producer.flush()
