from langchain_perplexity import ChatPerplexity 
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import List
from langchain_core.prompts import PromptTemplate

load_dotenv()

topic=input("Enter Topic:")
length=input("Enter Length:")

model=ChatPerplexity(model='sonar',temperature=0.4)

class validate(BaseModel):
    name:str=Field(description="enter Author name here")
    summary:str=Field(description="Write 2 line summary of the paragraph")
    keywords:List[str]=Field(description="Write top 4 keywords from the paragraph")

parser=PydanticOutputParser(pydantic_object=validate)

template=PromptTemplate(
    template="""Write a paragraph on {topic},write an dummy author name as well,keep the paragraph length {length} {format_instruction}""",
    input_variables=['Topic','length'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({
    'topic':topic,
     'length':length
})

result=model.invoke(prompt)

print(result)