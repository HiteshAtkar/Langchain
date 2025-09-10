from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

topic=input("Enter Topic:")

model=ChatPerplexity(model='sonar',temperature=0.5)

prompt=PromptTemplate(
    template="""write a large paragraph on {topic}""",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="""write 5 facts based on following paragraph\n {paragraph}""",
    input_variables=['paragraph']
)

parser=StrOutputParser()

chain= prompt | model | parser | prompt2 | model | parser

result=chain.invoke(topic)

print(result)