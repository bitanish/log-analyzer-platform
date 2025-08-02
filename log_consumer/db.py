from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch("http://elasticsearch:9200")

INDEX_NAME = "logs"

INDEX_MAPPING = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "level": {"type": "keyword"},
            "service": {"type": "keyword"},
            "user_id": {"type": "keyword"},
            "trace_id": {"type": "keyword"},
            "message": {"type": "text"},
            "meta": {
                "properties": {
                    "ip": {"type": "ip"}
                }
            }
        }
    }
}

def create_index_if_not_exists():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body=INDEX_MAPPING)
        print(f"Created index: {INDEX_NAME}")
    else:
        print(f"Index '{INDEX_NAME}' already exists")

def insert_logs_es(logs):
    actions = [
        {
            "_index": INDEX_NAME,
            "_source": log
        }
        for log in logs
    ]
    bulk(es, actions)