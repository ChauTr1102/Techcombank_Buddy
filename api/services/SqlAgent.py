from api.services import *


class SQLAgent:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)
        self.model_llm = ChatGoogleGenerativeAI(temperature=TEMPERATURE, model="gemini-2.5-flash-preview-05-20",
                                                api_key=apikey)

    def sql_decision(self, history, user_input):
        pass

    def sql_prompt_routing(self, user_input, history):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_folder}\n"),
                ("system", "**Instruction 2:**\n {prompt_template}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Context about relevant data:**\n{context}\n"),
                ("system", "**Context received from google search:**\n{web_search_context}\n"),
                ("system", "**Answer the question:** {question}"),
            ]
        )
        prompt = llm_prompt.format(prompt_folder=prompt_folder, prompt_template=prompt_template,
                                   chat_history=history, context=context, web_search_context=web_search_context,
                                   question=question)
        return prompt

