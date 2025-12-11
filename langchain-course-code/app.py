import os 
import openai 
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import HumanMessage


load_dotenv(find_dotenv())

# Not needed as now inferred
# openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-5-nano"


prompt = "How old is the Universe"

messages = [HumanMessage(content=prompt)]

llm = OpenAI(temperature=0.7)
chat_model = ChatOpenAI(temperature=0.7)


# print(llm.invoke("What is the weather in WA DC"))
# print("==========")

print(chat_model.invoke(messages).content)
# print(chat_model.invoke("What is the weather in WA DC"))




