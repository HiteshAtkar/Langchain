from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

document=[
    "My name is Hitesh",
    "I am AI/ML Engineer",
    "I live in Pune"
]

result=model.embed_documents(document)

print(str(result))

