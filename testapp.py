import streamlit as st
import streamlit.components.v1 as components
import base64
import io
import time

st.set_page_config(page_title="Voice Recorder with Auto-Stop", page_icon="🎤")

st.title("🎤 Voice Recorder with Auto-Stop")
st.write("Click 'Start Recording' and speak. Recording will automatically stop after 5 seconds of silence.")

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Initialize session state
    if 'recording_data' not in st.session_state:
        st.session_state.recording_data = None
    if 'recording_status' not in st.session_state:
        st.session_state.recording_status = "idle"

    # HTML and JavaScript for voice recording with auto-stop
    html_content = load_html_file('auto-stop.html')
    # Display the component
    result = components.html(html_code, height=300)

    # Handle the recorded audio
    if result and isinstance(result, dict) and 'audio_data' in result:
        st.session_state.recording_data = result['audio_data']
        st.session_state.recording_status = result['status']

    # Display recording info and options
    if st.session_state.recording_data:
        st.success("✅ Recording completed!")
        
        # Decode base64 audio data
        audio_bytes = base64.b64decode(st.session_state.recording_data)
        
        # Display audio player
        st.audio(audio_bytes, format='audio/wav')
        
        # Download button
        st.download_button(
            label="📥 Download Recording",
            data=audio_bytes,
            file_name=f"voice_recording_{int(time.time())}.wav",
            mime="audio/wav"
        )
        
        # Clear recording button
        if st.button("🗑️ Clear Recording"):
            st.session_state.recording_data = None
            st.session_state.recording_status = "idle"
            st.rerun()

# Instructions
st.markdown("---")
st.markdown("### 📝 Instructions")
st.markdown("""
1. **Click 'Start Recording'** to begin
2. **Speak clearly** into your microphone
3. **Recording will auto-stop** after 5 seconds of silence
4. **Manual stop** is available anytime with the Stop button
5. **Download** your recording when complete

**Note**: Make sure to allow microphone access when prompted by your browser.
""")

# Technical details
with st.expander("🔧 Technical Details"):
    st.markdown("""
    - **Voice detection**: Analyzes frequency range 85Hz-8000Hz (human voice)
    - **Background noise filtering**: Ignores sounds outside voice frequencies
    - **Energy ratio analysis**: 30% of sound energy must be in voice range
    - **Adaptive thresholds**: Minimum voice energy level of 15
    - **Auto-stop threshold**: 5 seconds without voice detection
    - **Browser compatibility**: Modern browsers with Web Audio API support
    - **Privacy**: All processing happens locally in your browser
    """)