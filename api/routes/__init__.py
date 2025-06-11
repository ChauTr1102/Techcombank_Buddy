from fastapi import UploadFile, File, Form, APIRouter, WebSocket,Request
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import shutil
import asyncio

router = APIRouter()

