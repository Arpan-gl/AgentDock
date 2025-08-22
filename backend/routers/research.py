from fastapi import HTTPException
from agents.portia_setup import research_investment_opportunities

def research_endpoint(payload: dict):
    result = research_investment_opportunities(payload.get("query", ""))
    try:
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
