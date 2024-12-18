import json
import os
from types import FunctionType
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)

def consume(topic: str, function: FunctionType ,mode='latest'):
    print(f"consumer listening to {topic}:")
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset=mode
    )
    for message in consumer:
        function(message)
