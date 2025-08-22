from fastapi import  HTTPException
from services.tavily_client import extract
from agents.portia_setup import tavily_search


def websearch(payload: dict):
    query = payload.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="Missing query")
    try:
        result = tavily_search(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def extract_endpoint(payload: dict):
    url = payload.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="Missing url")
    try:
        result = extract(url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
