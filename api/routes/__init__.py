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
from api.services.SqlAgent import SQLAgent
import io
from decimal import Decimal


from api.services.routing_agent import RoutingAgent
from api.database.database import SQLDatabase
from api.services.navigation_agent import NavigationAgent
from api.services.assistant_agent import AssistantAgent
from api.services.recommendation_agent import RecommendationAgent
load_dotenv()

stt = SpeechToText(apikey=os.getenv("API_KEY"))
router = APIRouter()
routing_agent = RoutingAgent(apikey=os.getenv("API_KEY"))
sql_db = SQLDatabase()
nav_agent = NavigationAgent(apikey=os.getenv("API_KEY"))
sql_agent = SQLAgent(apikey=os.getenv("API_KEY"))
assistant_agent = AssistantAgent(apikey=os.getenv("API_KEY"))
rec_agent = RecommendationAgent(apikey=os.getenv("API_KEY"))

class UserInput(BaseModel):
    user_input: str
    history: str


class Query(BaseModel):
    query: str


class TransactionQuery(BaseModel):
    query: str
    history: str

class TransferMoney(BaseModel):
    receiver: str
    note: str
    amount: Decimal