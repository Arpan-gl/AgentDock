# AgentDock

AgentDock is an AI-powered investment research assistant platform. It provides a backend API (FastAPI) and a frontend (Streamlit) for users to chat with an agent that can search the web, perform RAG (Retrieval-Augmented Generation), research investment opportunities, and interact with email and Slack.

---

## Features & APIs

### Backend (FastAPI)

- **POST `/chat`**
  - Main chat endpoint. Accepts a JSON payload with a `message` and optional fields.
  - The agent can:
    - Search the web (`websearch`)
    - Extract content from URLs (`extract_endpoint`)
    - Ingest and query documents (RAG)
    - Research investment opportunities
    - Search and send investment emails
    - Get and send Slack messages

#### Example Request
```json
POST /chat
{
  "message": "Tell me about AAPL stock",
  "query": "AAPL",
  "url": "https://...",
  "draft_id": "...",
  "channel_id": "...",
  "limit": 20
}
```

#### Example Response
```json
{
  "result": "...AI-generated response..."
}
```

---

## How to Run

### 1. Backend (FastAPI)

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

- Make sure to set the following environment variables (in a `.env` file or your system):
  - `GOOGLE_API_KEY`
  - `TAVILY_API_KEY`
  - `PORTIA_API_KEY`
  - `NEWSAPI_KEY` (optional)

### 2. Frontend (Streamlit)

```powershell
cd ../frontend
pip install -r requirements.txt
streamlit run app.py
```

- The frontend will connect to the backend at `http://localhost:8000/chat`.

---

## Using OpenAI (or Gemini) for LLM

This project uses [Portia](https://github.com/portia-ai/portia-sdk-python) as the agent framework. By default, it is configured to use Google Gemini (`GOOGLE_API_KEY`).

To use OpenAI models instead:
1. Set `PORTIA_LLM_PROVIDER=openai` in your `.env` file.
2. Add your `OPENAI_API_KEY` to the `.env` file.
3. Update the `Config` in `backend/agents/portia_setup.py`:
   ```python
   my_config = Config.from_default(
       llm_provider=LLMProvider.OPENAI,
       default_model="openai/gpt-4o",
       openai_api_key=settings.OPENAI_API_KEY
   )
   ```

---

## Project Structure

```
backend/
  main.py           # FastAPI app
  app_settings.py   # Settings & env
  agents/           # Portia agent setup
  routers/          # API endpoints
  services/         # Service logic
frontend/
  app.py            # Streamlit UI
```

---

## Credits
- Built with [FastAPI](https://fastapi.tiangolo.com/), [Streamlit](https://streamlit.io/), [Portia](https://github.com/portia-ai/portia-sdk-python)
