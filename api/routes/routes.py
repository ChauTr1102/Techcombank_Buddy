from api.routes import *


@router.get("/")
def read_root():
    return {
        "Xin chao, HEHEHE!"
    }


@router.websocket("/ws/audio")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()    # nhận chunk audio
        # xử lý hoặc forward audio chunk này
        await websocket.send_bytes(data)          # ví dụ phát lại


@router.post("/upload-audio")
async def receive_audio(request: Request):
    async def audio_generator():
        async for chunk in request.stream():
            yield chunk                      # mỗi chunk là bytes audio
    # Bạn có thể xử lý audio_generator() hoặc forward nó
    return StreamingResponse(audio_generator(), media_type="audio/wav")

