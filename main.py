from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
# Load API Key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Make sure it is in your .env file.")

client = openai.OpenAI(api_key=api_key)

app = FastAPI()

# Allow all origins (adjust for security in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": request.user_input}]
        )

        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}