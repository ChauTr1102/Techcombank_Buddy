from fastapi import UploadFile, File, Form, APIRouter, WebSocket,Request
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import shutil
import asyncio
from dotenv import load_dotenv, find_dotenv
import os
from api.services import speech_to_text
import io
load_dotenv()

stt = speech_to_text.SpeechToText(apikey=os.getenv("API_KEY"))
router = APIRouter()

