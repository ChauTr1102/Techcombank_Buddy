# import streamlit as st
#
# audio_value = st.audio_input("Record a voice message")
#
# if audio_value:
#     st.audio(audio_value)

import streamlit as st
from audiorecorder import audiorecorder
from google import genai

client = genai.Client(api_key="AIzaSyB2FVegtADHDDcG2klns-r0fP29uKaa1A8")

def transcribe_audio_file(audio_data):
    # Placeholder for transcription logic.
    # This should be replaced with your actual transcription code.
    myfile = client.files.upload(file=audio_data)
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=[
            "Lấy ra script của file audio này cho tôi, kể cả những từ ngữ tục tữu, chỉ trả về output thôi, không thêm cái gì khác",
            myfile]
    )
    return response.text

def main():
    st.title("Audio Recorder App")

    mode = st.selectbox("Select Mode", ["Record Audio", "Share Screen with DocuNexus", "Talk to DocuNexus"])

    if mode == "Record Audio":
        audio_data = audiorecorder("Record your question", "Click to record")

        if audio_data:
            st.audio(audio_data, format='audio/wav')
            transcript = transcribe_audio_file(audio_data)
            st.write("Transcript:")
            st.write(transcript)

    elif mode == "Talk to DocuNexus":
        st.write("Talk to DocuNexus mode selected.")
        # Add your additional logic for Talk to DocuNexus here

if __name__ == "__main__":
    main()