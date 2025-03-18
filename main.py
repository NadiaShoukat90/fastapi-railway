from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Enable CORS for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input model
class InputData(BaseModel):
    user_input: str

@app.post("/chat")
def chat_with_openai(data: InputData):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use "gpt-4o" or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": data.user_input}],
            api_key=OPENAI_API_KEY
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
