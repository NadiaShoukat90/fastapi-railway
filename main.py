from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input model
class InputData(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.post("/process")
def process_input(data: InputData):
    response_message = f"You entered: {data.user_input}"
    return {"response": response_message}
