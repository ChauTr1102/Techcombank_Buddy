from api.routes import *


@router.get("/")
def read_root():
    return {
        "Xin chao, HEHEHE!"
    }


@router.websocket("/ws/audio/")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()    # nhận chunk audio
        # xử lý hoặc forward audio chunk này
        await websocket.send_bytes(data)          # ví dụ phát lại


@router.post("/stt/")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    audio_buffer = io.BytesIO(audio_bytes)
    transcript = stt.retrieve_script(audio_buffer)  

    return transcript

@router.post("/sqlAgent/")
async def sql_agent(query: str):
    