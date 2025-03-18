import openai
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key!")

app = FastAPI()

# Enable CORS for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    user_input: str

@app.post("/chat")
async def chat_with_openai(data: InputData):
    try:
        client = openai.Client(api_key=OPENAI_API_KEY)  # ✅ Fix it
  # ✅ Use the new API format
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": data.user_input}]
        )
        return {"response": response.choices[0].message.content}
    except openai.OpenAIError as e:
        return {"error": f"OpenAI API Error: {str(e)}"}
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}
