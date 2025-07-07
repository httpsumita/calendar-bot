import streamlit as st
import requests

st.set_page_config(page_title="📅 Gemini Calendar Chat", page_icon="🤖")
st.title("📅 Gemini Calendar Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Schedule a meeting, cancel or check availability...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to FastAPI backend
    try:
        res = requests.post("http://localhost:8000/extract", json={"user_input": user_input})
        if res.status_code == 200:
            bot_response = res.json().get("response", "🤖 I didn’t understand that.")
        else:
            bot_response = f"❌ Error {res.status_code}: {res.text}"
    except Exception as e:
        bot_response = f"⚠️ Backend error: {e}"

    # Display bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
