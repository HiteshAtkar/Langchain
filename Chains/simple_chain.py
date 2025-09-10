from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatPerplexity(model='sonar',temperature=0.5)

topic=input("Enter Topic:")

prompt=PromptTemplate(
    template="""Write an paragraph on {topic}""",
        input_variables=['topic']
    )    

parser=StrOutputParser()

chain = prompt | model | parser

result=chain.invoke(topic)

print(result)