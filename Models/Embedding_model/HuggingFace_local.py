from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=HuggingFaceEndpointEmbeddings(repo_id='sentence-transformers/all-mpnet-base-v2',task='feature-extraction')

vector=model.embed_query("My name is Hitesh")
print(str(vector))