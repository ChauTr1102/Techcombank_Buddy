import streamlit as st
import streamlit.components.v1 as components
import base64
import tempfile
import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./endpoints.env")
SPEECH_TO_TEXT = os.getenv("SPEECH_TO_TEXT")

st.title("Ghi âm trực tiếp")

# Method 1: HTML Component with download
def voice_recorder_with_download():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .recorder-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px;
            }
            .record-button {
                background-color: #ff4b4b;
                color: white;
                border: none;
                border-radius: 50%;
                width: 80px;
                height: 80px;
                font-size: 16px;
                cursor: pointer;
                margin-bottom: 15px;
            }
            .record-button:hover {
                background-color: #ff6b6b;
            }
            .record-button.recording {
                background-color: #ff0000;
                animation: pulse 1s infinite;
            }
            .record-button.processing {
                background-color: #ffa500;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
            .status {
                margin: 10px 0;
                font-weight: bold;
            }
            .countdown {
                font-size: 24px;
                color: #ff4b4b;
                font-weight: bold;
            }
            .audio-player {
                margin-top: 15px;
            }
            .download-button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 10px;
                display: none;
            }
            .download-button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="recorder-container">
            <button id="recordButton" class="record-button">🎤<br>Record</button>
            <div id="status" class="status">Click to start recording</div>
            <div id="countdown" class="countdown" style="display: none;"></div>
            <audio id="audioPlayer" class="audio-player" controls style="display: none;"></audio>
            <button id="downloadButton" class="download-button">Download Audio</button>
        </div>

        <script>
            let mediaRecorder;
            let audioChunks = [];
            let audioContext;
            let analyser;
            let microphone;
            let silenceTimer;
            let countdownTimer;
            let countdownValue;
            let isRecording = false;
            let recordedBlob = null;

            const recordButton = document.getElementById('recordButton');
            const status = document.getElementById('status');
            const countdown = document.getElementById('countdown');
            const audioPlayer = document.getElementById('audioPlayer');
            const downloadButton = document.getElementById('downloadButton');

            // Voice activity detection parameters
            const SILENCE_THRESHOLD = -50;
            const SILENCE_DURATION = 3000;
            const CHECK_INTERVAL = 100;

            recordButton.addEventListener('click', toggleRecording);
            downloadButton.addEventListener('click', downloadAudio);

            async function toggleRecording() {
                if (!isRecording) {
                    await startRecording();
                } else {
                    stopRecording();
                }
            }

            async function startRecording() {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ 
                        audio: {
                            echoCancellation: true,
                            noiseSuppression: true,
                            autoGainControl: true
                        } 
                    });
                    
                    audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    analyser = audioContext.createAnalyser();
                    microphone = audioContext.createMediaStreamSource(stream);
                    microphone.connect(analyser);
                    
                    analyser.fftSize = 512;
                    const bufferLength = analyser.frequencyBinCount;
                    const dataArray = new Uint8Array(bufferLength);

                    mediaRecorder = new MediaRecorder(stream);
                    audioChunks = [];
                    
                    mediaRecorder.ondataavailable = event => {
                        audioChunks.push(event.data);
                    };
                    
                    mediaRecorder.onstop = processAudio;
                    
                    mediaRecorder.start();
                    isRecording = true;
                    
                    recordButton.textContent = '⏹️\\nStop';
                    recordButton.classList.add('recording');
                    status.textContent = 'Recording... Speak now!';
                    downloadButton.style.display = 'none';
                    
                    startVoiceActivityDetection(dataArray);
                    
                } catch (err) {
                    console.error('Error accessing microphone:', err);
                    status.textContent = 'Error: Could not access microphone';
                }
            }

            function startVoiceActivityDetection(dataArray) {
                function checkVoiceActivity() {
                    if (!isRecording) return;
                    
                    analyser.getByteFrequencyData(dataArray);
                    
                    let sum = 0;
                    for (let i = 0; i < dataArray.length; i++) {
                        sum += dataArray[i];
                    }
                    const average = sum / dataArray.length;
                    const dB = 20 * Math.log10(average / 255);
                    
                    if (dB > SILENCE_THRESHOLD) {
                        clearTimeout(silenceTimer);
                        clearInterval(countdownTimer);
                        countdown.style.display = 'none';
                        status.textContent = 'Recording... Speak now!';
                        countdownValue = 3;
                    } else {
                        if (!silenceTimer) {
                            startSilenceCountdown();
                        }
                    }
                    
                    setTimeout(checkVoiceActivity, CHECK_INTERVAL);
                }
                
                checkVoiceActivity();
            }

            function startSilenceCountdown() {
                countdownValue = 3;
                countdown.style.display = 'block';
                countdown.textContent = countdownValue;
                status.textContent = 'No voice detected. Auto-stopping in:';
                
                countdownTimer = setInterval(() => {
                    countdownValue--;
                    countdown.textContent = countdownValue;
                    
                    if (countdownValue <= 0) {
                        clearInterval(countdownTimer);
                        stopRecording();
                    }
                }, 1000);
                
                silenceTimer = setTimeout(() => {
                    stopRecording();
                }, SILENCE_DURATION);
            }

            function stopRecording() {
                if (!isRecording) return;
                
                isRecording = false;
                clearTimeout(silenceTimer);
                clearInterval(countdownTimer);
                silenceTimer = null;
                
                if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                    mediaRecorder.stop();
                }
                
                if (audioContext) {
                    audioContext.close();
                }
                
                recordButton.textContent = '🎤\\nRecord';
                recordButton.classList.remove('recording');
                recordButton.classList.add('processing');
                status.textContent = 'Processing audio...';
                countdown.style.display = 'none';
            }

            function processAudio() {
                recordedBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const audioUrl = URL.createObjectURL(recordedBlob);
                
                audioPlayer.src = audioUrl;
                audioPlayer.style.display = 'block';
                downloadButton.style.display = 'block';
                
                recordButton.classList.remove('processing');
                status.textContent = 'Audio recorded! You can play it above or download it below.';
            }

            function downloadAudio() {
                if (recordedBlob) {
                    const url = URL.createObjectURL(recordedBlob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'recorded_audio_' + new Date().getTime() + '.wav';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                }
            }
        </script>
    </body>
    </html>
    """
    
    components.html(html_code, height=350)

# Display the recorder
st.subheader("Step 1: Record Audio")
voice_recorder_with_download()

# File uploader for the recorded audio
st.subheader("Step 2: Upload Recorded Audio")
uploaded_file = st.file_uploader(
    "Upload the audio file you just recorded", 
    type=['wav', 'mp3', 'ogg', 'webm'],
    help="After recording, download the audio file and upload it here"
)

# Process uploaded audio
if uploaded_file is not None:
    st.success(f"Audio file uploaded: {uploaded_file.name}")
    
    # Read the uploaded file
    audio_bytes = uploaded_file.read()
    
    # Send POST request to FastAPI
    try:
        with st.spinner("Processing audio..."):
            res = requests.post(
                SPEECH_TO_TEXT,
                files={"file": (uploaded_file.name, audio_bytes, uploaded_file.type)}
            )
        
        if res.status_code == 200:
            st.success("Audio processed successfully!")
            transcript = res.json()
            st.text_area("Transcript", value=transcript, height=300)
            
            # Save transcript to session state
            if 'transcripts' not in st.session_state:
                st.session_state.transcripts = []
            st.session_state.transcripts.append({
                'filename': uploaded_file.name,
                'transcript': transcript,
                'timestamp': str(st.time())
            })
            
        else:
            st.error(f"Error: {res.status_code} - {res.text}")
            
    except Exception as e:
        st.error(f"Error sending audio to API: {str(e)}")

# Display previous transcripts
if 'transcripts' in st.session_state and st.session_state.transcripts:
    st.subheader("Previous Transcripts")
    for i, item in enumerate(reversed(st.session_state.transcripts)):
        with st.expander(f"Transcript {len(st.session_state.transcripts) - i}: {item['filename']}"):
            st.text(item['transcript'])
            st.caption(f"Processed at: {item['timestamp']}")