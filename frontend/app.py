import streamlit as st
import requests

st.set_page_config(page_title="Investment Research Chatbot", page_icon="📈")

st.title("📈 Investment Research Chatbot")
st.markdown("""
Ask me about any stock ticker (e.g., AAPL, TSLA, MSFT). I’ll fetch financials + latest news and summarize investment insights.
""")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def send_message_to_backend(message):
    try:
        resp = requests.post(
            "http://localhost:8000/chat",
            json={"message": message},
            timeout=30
        )
        if resp.status_code == 200:
            return resp.json().get("result", "No result returned.")
        else:
            return f"Error: {resp.json().get('detail', 'Unknown error')}"
    except Exception as e:
        return f"Backend error: {e}"

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter a stock ticker (e.g., AAPL)"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Researching..."):
        reply = send_message_to_backend(prompt)
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
