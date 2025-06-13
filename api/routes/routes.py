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

@router.post("/router_message/")
def router_message(user_input: UserInput):
    prompt = routing_agent.prompt_routing(user_input.user_input, user_input.history)
    result_router = routing_agent.routing(prompt)
    if result_router == "Navigation":
        pass
    elif result_router == "Recommendation":
        pass
    elif result_router == "Transaction":
        pass
    elif result_router == "Assistant":
        pass
    return result_router


@router.post("/test_db/")
def test_db():
    a = sql_db.test_db()
    return a
