from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

template=ChatPromptTemplate([
    ("system","You are {domain} expert AI Assistant"),
    ("human","Explain {topic} in simple terms")
    ])

model=ChatPerplexity(model="sonar",temperature=0.4)

prompt=template.invoke({'domain':'Science','topic':'ameaba'})

result=model.invoke(prompt)
print(prompt)

print(result.content)