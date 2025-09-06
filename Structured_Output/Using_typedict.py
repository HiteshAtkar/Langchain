from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from typing import TypedDict,Annotated,List

load_dotenv()

model=ChatPerplexity(model='sonar',temperature=0.5)

class review(TypedDict):
    summary:str
    sentiment:str
    keywords:Annotated[List[str],"Write Keywords from Review"]

structured_model=model.with_structured_output(review)

result=structured_model.invoke("""I recently upgraded to the latest iPhone, and the first thing that impressed me was the sleek design and lightweight feel. The display is crisp, colors pop, and watching videos feels almost cinematic. Performance-wise, apps open instantly and multitasking is effortless.

The camera is a highlight — night shots look clear, portraits have amazing depth, and the video stabilization is top-notch. Battery life is decent, lasting me through a busy workday with moderate use.

On the downside, the price is definitely on the higher side, and I wish Apple included faster charging in the box. Still, if you value reliability, security, and a premium experience, this iPhone is hard to beat.""")

print(result)