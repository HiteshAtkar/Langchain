from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda

load_dotenv()

review="The BMW M5 is such a nice car"

model=ChatPerplexity(model="sonar",temperature=0.5)

class validate(BaseModel):
    sentiment:Literal['positive','negetive']=Field(description="Give me sentiment of feedback")

parser=PydanticOutputParser(pydantic_object=validate)

parser2=StrOutputParser()

prompt=PromptTemplate(
    template="""Write a sentiment of following review\n {review} {format_instruction}""",
    input_variables=['review'],
    partial_variables={'format_instruction':parser.get_format_instructions}
)

prompt2=PromptTemplate(
    template="""Write an appropriate responce to this positive review \n {review}""",
    input_variables=['review']
)

prompt3=PromptTemplate(
    template="""Write an appropriate responce to this Negetive review \n {review}""",
    input_variables=['review']
)

schain= prompt | model | parser

bchain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser2 ),
    (lambda x:x.sentiment=='negetive', prompt3 | model | parser2 ),
    RunnableLambda(lambda x:'Not Able to find Sentiment')
)

chain= schain | bchain

result=chain.invoke(review)

print(result)
