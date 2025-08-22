from portia import LLMProvider, Portia, DefaultToolRegistry, Config
from app_settings import settings
from dotenv import load_dotenv
from portia.cli import CLIExecutionHooks

load_dotenv()

# Explicitly configure Portia to use Google as the LLM provider
my_config = Config.from_default(
    llm_provider=LLMProvider.GOOGLE,
    default_model = "google/gemini-2.0-flash",
    google_api_key=settings.GOOGLE_API_KEY
)

portia = Portia(
    config=my_config,
    tools = DefaultToolRegistry(my_config),
    execution_hooks=CLIExecutionHooks()
)

def tavily_search(query: str):
    plan = portia.plan(f"Search for investment opportunities using Tavily with query: {query}")
    return portia.run_plan(plan)

def research_investment_opportunities(query: str):
    plan = portia.plan(f"Research investment opportunities related to: {query}")
    return portia.run_plan(plan)

# Portia tool helpers
def search_investment_emails(query: str):
    plan = portia.plan(f"Search for investment-related emails containing the phrase: {query}")
    return portia.run_plan(plan)

def send_investment_email(draft_id: str):
    plan = portia.plan(f"Send the investment email with draft ID: {draft_id}")
    return portia.run_plan(plan)

def get_slack_conversation(channel_id: str, limit: int = 20):
    plan = portia.plan(f"Retrieve Slack conversation history for channel ID: {channel_id} with limit: {limit}")
    return portia.run_plan(plan)

def send_slack_message(target_id: str, message: str):
    plan = portia.plan(f"Send a Slack message to {target_id} with the content: {message}")
    return portia.run_plan(plan)