from typing import List, Dict

from dotenv import load_dotenv

import os

from kafka_settings.producer import produce

load_dotenv(verbose=True)
news_topic = os.environ['NEWS_TOPIC']

def produce_news(summeries:List[Dict]):
    produce(
        topic=news_topic,
        key="summeries_list",
        value=summeries
    )


if __name__ == '__main__':
    produce_news([{"test":"test"}])