from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

location=input("Enter Location:")

model=ChatPerplexity(model='sonar',temperature=0.4)

class validate(BaseModel):
    name:str=Field(description="Enter Name of Person")
    middlename:str=Field(description="Enter Middlename of Person")
    surname:str=Field(description="Enter Surname of Person")
    age:int=Field(description="Enter Age of person")

parser=PydanticOutputParser(pydantic_object=validate)

template=PromptTemplate(
    template="Write details of frictional person from {location}{format_instruction}",
    input_variables=['location'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= template | model | parser

final_result = chain.invoke({'location':location})

print(final_result)