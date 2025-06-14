from api.services import *


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
        prompt = llm_prompt.format(prompt_navigation=PROMPT_NAVIGATION, chat_history=history, user_input=user_input)
        return prompt

    def assitant_transaction_prompt(self, user_input, history, transaction_data):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_assistant}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Transaction data:**\n {transaction_data"),
                ("system", "**Answer the user's input:** {user_input}"),
            ]
        )
        prompt = llm_prompt.format(prompt_navigation=PROMPT_NAVIGATION, chat_history=history,
                                   transaction_data=transaction_data, user_input=user_input)
        return prompt
    def get_answer(self, prompt):
        result = self.model_llm.invoke(prompt)
        return result.content
