from api.services import *
import json

class AssistantAgent:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)
        self.model_llm = ChatGoogleGenerativeAI(temperature=TEMPERATURE, model="gemini-2.5-flash-preview-05-20",
                                                api_key=apikey)

    def assitant_prompt(self, user_input, history):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_assistant}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Answer the user's input:** {user_input}"),
            ]
        )
        prompt = llm_prompt.format(prompt_assistant=PROMPT_ASSISTANT, chat_history=history, user_input=user_input)
        return prompt

    def assitant_transaction_prompt(self, user_input, history, transaction_data):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_assistant}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Transaction data:**\n {transaction_data}\n"),
                ("system", "**Answer the user's input:** {user_input}"),
            ]
        )
        prompt = llm_prompt.format(prompt_assistant=PROMPT_ASSISTANT, chat_history=history,
                                   transaction_data=transaction_data, user_input=user_input)
        return prompt

    def get_answer(self, prompt):
        result = self.model_llm.invoke(prompt)
        return result.content

    def extract_transfer_info_from_text_ai(self, user_input):
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "{prompt}"),
                ("user", "{input}")
            ]
        )

        transfer_prompt = prompt_template.format_messages(
            prompt=PROMPT_TRANSFER_MONEY,
            input=user_input
        )
        try:
            result = self.model_llm.invoke(transfer_prompt)
            content = result.content.strip()

            # Tìm JSON trong nội dung trả về
            json_start = content.find('{')
            json_end = content.rfind('}')
            if json_start != -1 and json_end != -1:
                json_str = content[json_start:json_end + 1]
                data = json.loads(json_str)
                if data.get("action") == "transfer_money":
                    return [data.get("receiver"), data.get("amount"), data.get("note")]
        except Exception as e:
            print(f"[LLM EXTRACT ERROR] {e}")
        return None, None


    
