from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo" if you prefer
            messages=[{"role": "user", "content": request.user_input}]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
