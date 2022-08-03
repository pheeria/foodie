import os, re
from elasticsearch import Elasticsearch


def search_client() -> Elasticsearch:
    return Elasticsearch("http://localhost:9200")
