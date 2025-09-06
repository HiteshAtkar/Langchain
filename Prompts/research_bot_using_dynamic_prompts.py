from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


paper_name=input("Enter Paper Title:")
length=input("Enter Paper Length (short /medium/large):")
style=input("Enter Paper Style(begineer/advanced/expert):")

template=PromptTemplate(
    template="""Summarize the research paper titled {paper_name} with following fashion
                Explanation length sould be: {length}
                explanation style should be: {style}  
                  1.Mathematical Details:
                        -include formulas if present
                        -explain mathematical concepts if exists 
                        
                   2.Anologies
                        -use relatable anolagies to simplify complex ideas
                
                if certain information is missing then responce with:insufficient information""",
    input_variables=['paper_name','length','style']
)

prompt=template.invoke({
    'paper_name':paper_name,
    'length':length,
    'style':style
})

model=ChatPerplexity(model="sonar",temperature=0.4,max_tokens=100)

result=model.invoke(prompt)

print(result)