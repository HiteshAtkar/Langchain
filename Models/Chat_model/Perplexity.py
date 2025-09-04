from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()

model= ChatPerplexity(model='sonar',temperature=0.4)

query=input("Ask Perplexity:")
result=model.invoke(query)
print("Ans\n",result.content)