from langchain_community.document_loaders import TextLoader
from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader=TextLoader('human.txt',encoding='utf-8')
docs=loader.load()

prompt=PromptTemplate(
    template="Write a 2 line summary of following paragraph\n{text}",
    input_variables=['text']
)

model=ChatPerplexity(model='sonar',temperature=0.4)

parser=StrOutputParser()

chain= prompt | model | parser

result=chain.invoke(docs[0])

print(result)