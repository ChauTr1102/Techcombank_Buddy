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
        prompt_nav = nav_agent.navigation_prompt(user_input.user_input, user_input.history)
        result_nav = nav_agent.nav_direction(prompt_nav)
        return result_nav
    elif result_router == "Recommendation":
        return "Recommendation"
    elif result_router == "TransactionHistory":
        transaction_prompt = sql_agent.sql_prompt_routing(user_input.user_input, user_input.history)
        sql_query_result = sql_agent.sql_result_from_llm(transaction_prompt)
        fetched_data = sql_db.execute_query(sql_query_result)
        if len(fetched_data) != 0:
        # lấy prompt và lấy kết quả từ llm
            assistant_prompt = assistant_agent.assitant_transaction_prompt(user_input.user_input, user_input.history, fetched_data)
            answer = assistant_agent.get_answer(assistant_prompt)
            return answer
        else:
            note = "`Note from server: Bạn vẫn có thể truy cập vào database để tìm kiếm thông tin nhưng, không tìm thấy dữ liệu trong database đối với câu hỏi của người dùng`"
            assistant_prompt = assistant_agent.assitant_transaction_prompt(user_input.user_input, user_input.history, note)
            answer = assistant_agent.get_answer(assistant_prompt)
            return answer
    elif result_router == "Assistant":
        assist_prompt = assistant_agent.assitant_prompt(user_input.user_input, user_input.history)
        answer = assistant_agent.get_answer(assist_prompt)
        return answer


@router.post("/test_db/")
def test_db():
    a = sql_db.test_db()
    return a


@router.post("/transaction_query/")
def transaction_query(query: TransactionQuery):
    transaction_prompt = sql_agent.sql_prompt_routing(query.query, query.history)
    sql_query_result = sql_agent.sql_result_from_llm(transaction_prompt)
    fetched_data = sql_db.execute_query(sql_query_result)
    # lấy prompt và lấy kết quả từ llm
    assistant_prompt = assistant_agent.assitant_transaction_prompt(query.query, query.history, fetched_data)
    answer = assistant_agent.get_answer(assistant_prompt)

    return sql_query_result, answer




