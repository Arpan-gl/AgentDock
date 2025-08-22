from fastapi import HTTPException
from services.rag_store import rag_store
import glob
import os

def rag_ingest():
    try:
        doc_paths = glob.glob(os.path.join("data", "seed_docs", "*.txt"))
        rag_store.ingest(doc_paths)
        return {"status": "ingested", "count": len(doc_paths)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def rag_query(payload: dict):
    query = payload.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="Missing query")
    try:
        results = rag_store.query(query)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
