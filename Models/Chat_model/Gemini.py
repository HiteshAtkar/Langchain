from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')

query=input("Ask AI:")
result=model.invoke(query)
print(result.content)