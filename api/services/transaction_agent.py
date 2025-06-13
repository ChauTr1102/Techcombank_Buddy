from api.services import *

class TransactionAgent:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)
        self.model_llm = ChatGoogleGenerativeAI(temperature=TEMPERATURE, model="gemini-2.5-flash-preview-05-20",
                                                api_key=apikey)
    def transaction_prompt(self, user_input):
        