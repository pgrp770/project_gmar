from typing import List

from elasticsearch.helpers import bulk

from data_management_app.db.elastic_db.database import elastic_client


def create_summery(summeries_actions: List[dict]):
    return bulk(elastic_client, summeries_actions)
