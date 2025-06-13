# import streamlit as st
# st.set_page_config(page_title="Techcombank Buddy Multi Agent")

# import streamlit.components.v1 as components
# import base64
# import io
# import time
# import os
# import requests
# from dotenv import load_dotenv
# from streamlit_extras.bottom_container import bottom
# from streamlit_float import *
# float_init()
# load_dotenv(dotenv_path="./endpoints.env")

# SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")

# empty_col_1, input_col, empty_col = st.columns([1.25, 8, 1.25], vertical_alignment="top")
# with bottom():
#     st.session_state["question"] = st.chat_input("Xin chào bạn, mình là Techcombank Buddy!")


#     audio_data = st.audio_input(label="Bấm để nói chuyện", key="audio_input")
#     if audio_data:
#         audio_bytes = audio_data.getvalue()
#         # Gửi POST request đến FastAPI
#         res = requests.post(
#             SPEECH_TO_TEXT,
#             files={"file": ("audio.wav", audio_bytes, "audio/wav")}
#         )
#         st.session_state["question"] = res.json()
#         del st.session_state["audio_input"]
#         audio_data = None


# with input_col:
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["output"])

#     if st.session_state["question"]:
#         st.chat_message("user").markdown(st.session_state["question"])
#         st.session_state.messages.append({"role": "user", "output": st.session_state["question"]})
#     if "question" in st.session_state and st.session_state["question"]:
#         with st.chat_message("assistant"):
#             assistant_message = st.empty()
#             user_input = {
#                 "user_input": str(st.session_state["question"]),
#                 "history": " "
#             }
#             response = requests.post(url=os.getenv("ROUTER_MESSAGE"), json=user_input)
#             assistant_message.markdown(response.json())
#             st.session_state.messages.append({"role": "assistant", "output": response.json()})

import streamlit as st
st.set_page_config(page_title="Techcombank Buddy Multi Agent")

import os
import requests
from dotenv import load_dotenv
from streamlit_extras.bottom_container import bottom
from streamlit_float import *
float_init()
load_dotenv(dotenv_path="./endpoints.env")

SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")
ROUTER_MESSAGE = os.getenv("ROUTER_MESSAGE")

# Khởi tạo session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "text_input" not in st.session_state:
    st.session_state["text_input"] = None

if "voice_input" not in st.session_state:
    st.session_state["voice_input"] = None

if "input_processed" not in st.session_state:
    st.session_state["input_processed"] = True  # Đã xử lý xong thì không lặp

# Giao diện
empty_col_1, input_col, empty_col = st.columns([1.25, 8, 1.25], vertical_alignment="top")

with bottom():
    # 🧠 Text input
    text = st.chat_input("Xin chào bạn, mình là Techcombank Buddy!")
    if text:
        st.session_state["text_input"] = text
        st.session_state["input_processed"] = False

    # 🎙️ Voice input
    audio_data = st.audio_input(label="Bấm để nói chuyện", key="audio_input")
    if audio_data:
        audio_bytes = audio_data.getvalue()
        res = requests.post(
            SPEECH_TO_TEXT,
            files={"file": ("audio.wav", audio_bytes, "audio/wav")}
        )
        if res.ok:
            st.session_state["voice_input"] = res.json()
            st.session_state["input_processed"] = False
        del st.session_state["audio_input"]

# Xử lý chính
with input_col:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["output"])

    if not st.session_state["input_processed"]:
        # Ưu tiên text input nếu có, nếu không thì voice
        final_input = st.session_state["text_input"] or st.session_state["voice_input"]
        if final_input:
            st.chat_message("user").markdown(final_input)
            st.session_state.messages.append({"role": "user", "output": final_input})

            with st.chat_message("assistant"):
                assistant_message = st.empty()
                payload = {
                    "user_input": str(final_input),
                    "history": " "
                }
                response = requests.post(url=ROUTER_MESSAGE, json=payload)
                if response.ok:
                    reply = response.json()
                    assistant_message.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "output": reply})
                else:
                    assistant_message.markdown("❌ Lỗi khi gửi dữ liệu đến API.")

            # ✅ Sau khi xử lý xong, reset cả 2 input
            st.session_state["text_input"] = None
            st.session_state["voice_input"] = None
            st.session_state["input_processed"] = True
