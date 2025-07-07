# agent.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

# ✅ Initialize OpenRouter model correctly
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    base_url="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY")  # ✅ Use openai_api_key, not api_key
)

# ✅ Create prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that helps users book calendar appointments.

Extract the following from user message:
- Intent (Is it about booking, canceling, checking?)
- Date (in ISO format: YYYY-MM-DD)
- Time (in 24-hour format, HH:MM)
- Duration (in minutes)
- Title of event

Message: {user_input}

Respond in pure JSON (all keys and stringd must use double quotes) with keys: intent, date, time, duration, title.
yyy
""")

# ✅ Create LangChain runnable chain
chain = prompt | llm | StrOutputParser()

# ✅ Real-time input handler
def extract_booking_details(user_input: str):
    # Ensure you're passing a plain string, NOT a Field or object
    return chain.invoke({"user_input": user_input})
