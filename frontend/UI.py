import streamlit as st
import streamlit.components.v1 as components
import base64
import io
import time
from google import genai
import os 
import requests
from dotenv import load_dotenv
load_dotenv(dotenv_path="./endpoints.env")

SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")

st.title("Ghi âm trực tiếp")
audio_data = st.audio_input("Nhấn để ghi âm")  # Thu âm từ mic :contentReference[oaicite:2]{index=2}

# Cấu hình API key

if audio_data:
    audio_bytes = audio_data.getvalue()
        # Gửi POST request đến FastAPI
    res = requests.post(
        SPEECH_TO_TEXT,
        files={"file": ("audio.wav", audio_bytes, "audio/wav")}
    )
    st.text_area("Transcript", value=res.json(), height=300)

