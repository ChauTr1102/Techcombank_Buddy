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
        recommendation_prompt = rec_agent.recommendation_prompt(user_input.user_input, user_input.history)
        recommendation_result = rec_agent.recommending(recommendation_prompt)
        if recommendation_result == "No":
            return "`Note from server: Không tìm thấy sản phẩm nào phù hợp với yêu cầu của bạn`"
        Query = "SELECT * FROM products WHERE category = '" + recommendation_result + "'limit 20;"
        rule_fetched_data = sql_db.execute_query(Query)
        assistant_prompt_rec = assistant_agent.assitant_transaction_prompt(user_input.user_input, user_input.history, rule_fetched_data)
        answer_rec = assistant_agent.get_answer(assistant_prompt_rec)
        return answer_rec
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


@router.post("/transfer_money_extraction/")
def transfer_money_extraction(user_input: UserInput):
    receiver, amount, note = assistant_agent.extract_transfer_info_from_text_ai(user_input.user_input)
    return receiver, amount, note


@router.post("/transfer_money/")
def transfer_money(transfer_info: TransferMoney):
    sql_db.insert_transfer_money_history(transfer_info.receiver, transfer_info.note, transfer_info.amount)
    return 1


@router.get("/transaction_history/")
def get_transaction_history():
    transaction_history = sql_db.get_transaction_history()
    return transaction_history


@router.post("/customer_segment/", response_model=CustomerSegmentResponse)
async def get_customer_segment(request: UserRequest):
    """Lấy thông tin phân khúc và gợi ý sản phẩm cho khách hàng"""
    try:
        # Tải dữ liệu
        customer_data = rcm_model.load_customer_data()
        products_data = rcm_model.load_product_data()
        processed_data = rcm_model.preprocess_for_segmentation(customer_data)

        # Dự đoán phân khúc
        clusters = rcm_model.load_and_predict(processed_data)
        customer_data['segment'] = clusters

        # Lấy thông tin phân khúc
        result = rcm_model.get_customer_segment_from_existing(customer_data, products_data, request.user_id)
        if result is None:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy khách hàng với user_id: {request.user_id}")

        return result

    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))


@router.post("/get_explain_for_eight_recommendation/")
def get_explain_for_eight_recommendation(data: RecommendationData):
    rcm_prompt = rcm_model.recommendation_prompt(data.data)
    result = rcm_model.rcm_explain(rcm_prompt)
    return result



