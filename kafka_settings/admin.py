import os

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)
news_topic = os.environ['NEWS_TOPIC']


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
    create_topic(news_topic)


if __name__ == '__main__':
    init_topics()
