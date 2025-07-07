import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

for model in models:
    print(f"Model name: {model.name}")
    print(f"Supported methods: {model.supported_generation_methods}")
    print("-" * 50)
