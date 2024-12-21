import os
from dotenv import load_dotenv

from elasticsearch import Elasticsearch

load_dotenv(verbose=True)

elastic_client = Elasticsearch(os.environ["ELASTIC_URL"])
