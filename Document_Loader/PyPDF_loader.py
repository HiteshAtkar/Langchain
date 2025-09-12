from langchain_community.document_loaders import PyPDFLoader
from langchain_perplexity import ChatPerplexity
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


loader=PyPDFLoader('Hitesh_Atkar_Summary.pdf')

docs=loader.load()

prompt=PromptTemplate(
    template="Imagine you are a Chat bot which give 1 line responces on my questions to ans my question i provided you my textual info use that to ans my questions\n{text}\n\n{question}",
    input_variables=['text','question']
)

model=ChatPerplexity(model='sonar',temperature=0.4)

parser=StrOutputParser()

while(True):
    question=input("Ask AI:")
    if(question=='exit'):
        break
    else:
        chain= prompt | model | parser
        result=chain.invoke({'text':docs[0].page_content,'question':question})
        print("AI:",result)
