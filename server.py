from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.onyx_core import ONYXNOKAMI


env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

app = FastAPI()
bot = ONYXNOKAMI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "ONYX is awake"}


@app.post("/chat")
def chat(request: ChatRequest):
    reply = bot.handle(request.message)
    return {"reply": reply}