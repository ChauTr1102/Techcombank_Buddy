from fastapi import UploadFile, File, Form, APIRouter, WebSocket,Request
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import shutil
import asyncio
from dotenv import load_dotenv, find_dotenv
import os
from api.services.speech_to_text import SpeechToText
import io

from api.services.routing_agent import RoutingAgent
from api.database.database import SQLDatabase
load_dotenv()

stt = SpeechToText(apikey=os.getenv("API_KEY"))
router = APIRouter()
routing_agent = RoutingAgent(apikey=os.getenv("API_KEY"))
sql_db = SQLDatabase()

class UserInput(BaseModel):
    user_input: str
    history: str


class Query(BaseModel):
    query: str

