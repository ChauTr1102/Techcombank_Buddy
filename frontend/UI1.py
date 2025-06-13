import streamlit as st
st.set_page_config(page_title="Techcombank Buddy Multi Agent")

import streamlit.components.v1 as components
import base64
import io
import time
import os
import requests
from dotenv import load_dotenv
from streamlit_extras.bottom_container import bottom
from streamlit_float import *
float_init()
load_dotenv(dotenv_path="./endpoints.env")


SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")

audio_data = st.audio_input(label="")



    # st.text_area("Transcript", value=res.json(), height=300)

empty_col_1, input_col, empty_col = st.columns([1.25, 8, 1.25], vertical_alignment="top")
with bottom():
    st.session_state["question"] = st.chat_input("Xin chào bạn, mình là Techcombank Buddy!")
    if audio_data:
        audio_bytes = audio_data.getvalue()
            # Gửi POST request đến FastAPI
        res = requests.post(
            SPEECH_TO_TEXT,
            files={"file": ("audio.wav", audio_bytes, "audio/wav")}
        )
        st.session_state["question"] = res.json()
with input_col:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

        # chat_input_container = st.container()
        # with chat_input_container:
    if st.session_state["question"]:
        st.chat_message("user").markdown(st.session_state["question"])
        st.session_state.messages.append({"role": "user", "output": st.session_state["question"]})
        with st.chat_message("assistant"):
            assistant_message = st.empty()
# css_chat_input_container = float_css_helper(bottom="27px", z_index="100")
# chat_input_container.float(css_chat_input_container)

st.markdown(
    """
    <style>
    div[data-testid="stAudio"] audio {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
