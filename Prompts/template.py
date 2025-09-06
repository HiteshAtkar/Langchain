from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

template=ChatPromptTemplate([
    ('system','You are a helful {domain} expert'),
    ('human','Explain in simple term, what is {topic}')
])

prompt=template.invoke({'domain':'AI','topic':'Model overfitting'})
print(prompt)
