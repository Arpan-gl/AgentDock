from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, HTTPException
from routers.rag import rag_ingest,rag_query
from agents.portia_setup import portia, search_investment_emails, send_investment_email, send_slack_message, get_slack_conversation
from routers.search import websearch,extract_endpoint
from routers.research import research_endpoint
    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat_endpoint(payload: dict):
    message = payload.get("message", "")
    plan = portia.plan(f"""
                       Chat with the investment research agent. User message: {message}
                        with some tools access:
                        "Tavily Search websearch":{websearch(payload)},
                        "Tavily Search extract":{extract_endpoint(payload)},
                        "RAG Ingest":{rag_ingest()},
                        "RAG Query":{rag_query(payload)},
                        "Research":{research_endpoint(payload)},
                        "Send Investment Email":{send_investment_email(payload.get("draft_id",""))},
                        "Get Slack Conversation":{get_slack_conversation(payload.get("channel_id",""), payload.get("limit",20))},
                        "Search Investment Emails":{search_investment_emails(payload.get("query",""))},
                        "Send Slack Message":{send_slack_message(payload.get("channel_id",""), payload.get("message",""))}
                       """)
    result = portia.run_plan(plan)
    try:
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))