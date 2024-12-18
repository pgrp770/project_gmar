import os
from typing import List
import toolz as t
from dotenv import load_dotenv
import faust

# run in the terminal
# faust -A example  worker -l info -p 6609

# Load environment variables
load_dotenv(verbose=True)

# Faust app for stream processing
app = faust.App(
    'classes_streaming',  # App name
    broker=os.environ['BOOTSTRAP_SERVERS'],  # Kafka broker
    value_serializer='json'  # Message value format
)

# Define a Kafka topic to consume from
classes_topic = app.topic(os.environ["CLASSES_TOPIC"])

processed_classes_topic_neo4j = app.topic(os.environ["NEO4J_CLASSES_TOPIC"])
processed_classes_topic_postgres = app.topic(os.environ["POSTGRES_CLASSES_TOPIC"])

def extract_id_from_classes(classes:List):
    return t.pipe(
        classes,
        t.partial(map, lambda x: x['id']),
        list
    )

# Stream processing agent
@app.agent(classes_topic)
async def process_person(messages):
    async for message in messages:


        await processed_classes_topic_neo4j.send(value=extract_id_from_classes(message))
        await processed_classes_topic_postgres.send(value=message)

if __name__ == '__main__':
    # Run Faust in one thread
    app.main()
