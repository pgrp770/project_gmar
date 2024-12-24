from typing import List, Dict

from data_management_app.db.elastic_db.repositories.summery_repository import create_bulk
from data_management_app.services.insert_elastic_service.bulk_service import from_list_to_actions


def main_flow_news_consumer(summeries):
    create_bulk(from_list_to_actions("summeries", summeries.value))