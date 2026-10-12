# fast api code 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import uvicorn

from chatbot import generate_response


# Create FastAPI application
app = FastAPI(
    title="AI Personality Chatbot API",
    description="Chat with Funny, Sad, Angry, or Normal AI",
    version="1.0.0",
)


# Define the request data structure
class ChatRequest(BaseModel):
    mode: Literal["funny", "sad", "angry", "normal"] = "normal"

    history: list[dict[str, str]] = Field(
        default_factory=list
    )

    message: str = Field(
        min_length=1,
        max_length=10000
    )


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "AI Personality Chatbot API is running"
    }


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    try:
        answer = generate_response(
            mode=request.mode,
            history=request.history,
            prompt=request.message,
        )

        return {
            "reply": answer
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate response: {exc}",
        )


# creating a http server 


if __name__ == "__main__":
   

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )


