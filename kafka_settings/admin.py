import os
import time

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)
list_topics = [
    os.environ['NEO4J_TEACHERS_TOPIC'],
    os.environ['NEO4J_CLASSES_TOPIC'],
    os.environ['NEO4J_RELATIONS_TOPIC'],
    os.environ['POSTGRES_STUDENT_PROFILE_TOPIC'],
    os.environ['POSTGRES_STUDENT_LIFE_STILE_TOPIC'],
    os.environ['POSTGRES_STUDENT_PERFORMANCE_TOPIC'],
    os.environ['POSTGRES_TEACHER_TOPIC'],
    os.environ['POSTGRES_CLASSES_TOPIC'],
    os.environ['CLASSES_TOPIC'],
    os.environ['TEACHER_TOPIC'],
    os.environ['ELASTIC_TOPIC']
]

def create_topic(topic_name):
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    new_member_topic = NewTopic(
        name=topic_name,
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    try:
        client.create_topics([new_member_topic])
        print(f"create topic {topic_name}")
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()
def init_topics():
    for topic in list_topics:
        create_topic(topic)


if __name__ == '__main__':
    init_topics()
