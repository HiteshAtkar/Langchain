from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
     task='text-generation',
     pipeline_kwargs=dict(
         temperature=0.4,
         max_new_tokens=100
     )
)

model= ChatHuggingFace(llm=llm)

while(True):
     query=input("You:")
     if(query=="exit"):
         break
     else:
          result=model.invoke(query) 
          print("Bot:",result.content)


