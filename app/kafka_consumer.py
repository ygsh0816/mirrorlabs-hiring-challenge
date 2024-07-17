# app/kafka_consumer.py
import json
import os
import threading
import time

from kafka import KafkaConsumer
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")


class KafkaConsumerService:
    def __init__(self, topic, broker_url):
        self.topic = topic
        self.broker_url = broker_url
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.broker_url,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.thread = threading.Thread(target=self.consume_messages)
        self.thread.daemon = True
        self.running = False
        self.user_locations = {}

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False
        self.consumer.close()

    def consume_messages(self):
        while self.running:
            for message in self.consumer:
                try:
                    value = message.value
                    self.user_locations[value['user_id']] = {
                        'lat': value['lat'],
                        'long': value['long'],
                        'timestamp': value['timestamp']
                    }
                    print(f"Received message: {value}")
                except json.JSONDecodeError as e:
                    print(f"Failed to decode message: {e}")
                if not self.running:
                    break
            time.sleep(1)  # Prevents CPU intensive loop if no messages


kafka_consumer_service = KafkaConsumerService(KAFKA_TOPIC, KAFKA_BROKER_URL)
