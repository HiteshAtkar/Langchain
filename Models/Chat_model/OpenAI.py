from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4',temperature=0.4,max_completion_tokens=50)

query=input("Ask AI:")
result=model.invoke(query)
print(result.content)
