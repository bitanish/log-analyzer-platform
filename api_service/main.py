from fastapi import FastAPI, Query, HTTPException
from elasticsearch import AsyncElasticsearch
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Elasticsearch client
es = AsyncElasticsearch(hosts=["http://elasticsearch:9200"])  # use 'elasticsearch' if Docker

# Pydantic query model
class LogFilterParams(BaseModel):
    level: Optional[str] = None
    service: Optional[str] = None
    user_id: Optional[str] = None
    start_time: Optional[str] = None  # ISO format
    end_time: Optional[str] = None
    size: int = 50
    page: int = 1

@app.get("/logs/filter")
async def filter_logs(
    level: Optional[str] = Query(None),
    service: Optional[str] = Query(None),
    user_id: Optional[str] = Query(None),
    start_time: Optional[str] = Query(None),
    end_time: Optional[str] = Query(None),
    size: int = Query(50, ge=1, le=1000),
    page: int = Query(1, ge=1)
):
    must_clauses = []

    if level:
        must_clauses.append({"match": {"level": level}})
    if service:
        must_clauses.append({"match": {"service": service}})
    if user_id:
        must_clauses.append({"match": {"user_id": user_id}})
    if start_time and end_time:
        must_clauses.append({
            "range": {
                "timestamp": {
                    "gte": start_time,
                    "lte": end_time
                }
            }
        })

    query = {
        "query": {
            "bool": {
                "must": must_clauses
            }
        },
        "from": (page - 1) * size,
        "size": size,
        "sort": [
            {"timestamp": "desc"}
        ]
    }

    try:
        response = await es.search(index="logs", body=query)
        hits = response["hits"]["hits"]
        return [hit["_source"] for hit in hits]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
