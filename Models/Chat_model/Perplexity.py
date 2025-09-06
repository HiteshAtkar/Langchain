from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()

model= ChatPerplexity(model='sonar',temperature=0.4,max_tokens=50)

query=input("Ask Perplexity:")
result=model.invoke(query)
print("Ans:",result.content)