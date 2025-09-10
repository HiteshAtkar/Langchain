from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
from langchain_core.prompts import PromptTemplate

load_dotenv()

topic=input("Enter Topic Name:")
length=input("Enter Length of topic(short/mid/long):")
genre=input("Enter genre of the topic(comedy,horror,action,sci-fi):")

model=ChatPerplexity(model='sonar',temperature=0.5)

template=PromptTemplate(
    template="""Write a 10 line paragraph on {topic},with author name.lenght of the paragraph should be {length} and genre of paragraph should be {genre}.write an dummy author name along with it""",
    input_variables=['topic','lenght','genre']
)

prompt=template.invoke({
    'topic':topic,
    'length':length,
    'genre':genre
})

class validation(TypedDict):
    author:Optional[str]=None
    summary:Annotated[str,"Summary of the paragraph"]
    
strctured=model.with_structured_output(validation)
result=strctured.invoke(prompt)
print(result)