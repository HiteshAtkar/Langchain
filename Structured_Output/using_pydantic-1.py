from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Optional,List

load_dotenv()

class validate(BaseModel):
    title:str=Field(description="Title of the Paragraph")
    summary:str=Field(description="Write 2 line summary of the paragraph")
    author:Optional[str]=Field(default=None,description="Write the name of author of this Paragraph if Available")
    keyword:List[str]=Field(description="Write Top 3 keyword from paragraph")
    adv:List[str]=Field(description="Write conclusion in 3 short point")


model=ChatPerplexity(model='sonar',temperature=0.5)
structured_op=model.with_structured_output(validate)
result=structured_op.invoke("""
Quantum computing is a revolutionary paradigm that seeks to harness the counterintuitive principles of quantum mechanics—such as superposition, entanglement, and interference—to perform computations far beyond the capabilities of classical computers. Unlike traditional bits, which exist as 0 or 1, quantum bits or qubits can exist in multiple states simultaneously, allowing quantum computers to explore many possible solutions in parallel. This property opens doors to breakthroughs in cryptography, molecular modeling, drug discovery, financial modeling, and optimization problems that are computationally intractable for even the most powerful supercomputers today. However, building large-scale quantum computers remains an enormous challenge, primarily due to qubit fragility, noise, and the complexity of error correction. Despite these hurdles, rapid progress is being made by both academic researchers and leading technology companies, with the hope that in the near future, quantum advantage will be achieved in practical, real-world applications.
Author: David Deutsch""")

print(result)