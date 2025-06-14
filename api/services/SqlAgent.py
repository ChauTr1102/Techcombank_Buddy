from api.services import *


class SQLAgent:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)
        self.model_llm = ChatGoogleGenerativeAI(temperature=TEMPERATURE, model="gemini-2.5-flash-preview-05-20",
                                                api_key=apikey)

    def sql_prompt(self, user_input, history):
        llm_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "**Instruction 1:**\n {prompt_routing}\n"),
                ("system", "**Chat history:**\n {chat_history}\n"),
                ("system", "**Answer the question:** {user_input}"),
            ]
        )
        prompt = llm_prompt.format(prompt_routing=PROMPT_ROUTING, chat_history=history, user_input=user_input)

        return prompt
    
    def sql_prompt(self, prompt):
        result = self.model_llm.invoke(prompt)
        return result.content
        
    def sql_pull(self, sql_query):
        try:
            result = execute_sql_query(sql_query)  
            return result
        except Exception as e:
            return f"An error occurred while executing the SQL query: {str(e)}"
