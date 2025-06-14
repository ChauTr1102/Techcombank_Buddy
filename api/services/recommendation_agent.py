from api.services import *

class NavigationAgent:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)
        self.model_llm = ChatGoogleGenerativeAI(temperature=TEMPERATURE, model="gemini-2.5-flash-preview-05-20",
                                                api_key=apikey)
    def recommendation_prompt(self, user_input):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_routing}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Answer the question:** {user_input}"),
            ]
        )
        prompt = llm_prompt.format(prompt_routing=PROMPT_ROUTING, chat_history=history, user_input=user_input)
        return prompt
