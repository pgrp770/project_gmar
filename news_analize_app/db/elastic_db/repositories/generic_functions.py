from typing import List

from elasticsearch.helpers import bulk

from news_analize_app.db.elastic_db.database import elastic_client


def create_butch(generic_actions: List[dict]):
    print(f"insert {len(generic_actions)} actinos to database")
    return bulk(elastic_client, generic_actions)
