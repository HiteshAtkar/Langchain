from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

location=input("Enter Location:")

model=ChatPerplexity(model='sonar',temperature=0.5)

class validate(BaseModel):
    name:str=Field(description="Enter Name of person here")
    middlename:str=Field(description="Enter Middlename of person here")
    surname:str=Field(description="Enter person surname of person")

parser=PydanticOutputParser(pydantic_object=validate)

template=PromptTemplate(
    template="""write frictional name of a person from {location},{format_instruction}""",
    input_variables=['location'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({
    'location':location
})

result=model.invoke(prompt)

print(result.content)

