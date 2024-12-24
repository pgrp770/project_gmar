from typing import Callable

from dotenv import load_dotenv
import os

from data_management_app.services.kafka_services.consumer_services.consume_news_service import main_flow_news_consumer
from kafka_settings.consumer import consume

load_dotenv(verbose=True)
news_topic = os.environ['NEWS_TOPIC']

def consume_classes(func: Callable):
    consume(
        topic=news_topic,
        function=func
    )


if __name__ == '__main__':
    consume_classes(main_flow_news_consumer)
