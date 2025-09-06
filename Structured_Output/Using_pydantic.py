from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import List

load_dotenv()

model=ChatPerplexity(model="sonar",temperature=0.4)

class review(BaseModel):
    summary:str=Field(description="Write 2 line short summary of review")
    sentiment:str=Field(description="Write sentiment of the review from Pos or neg")
    keyword:List[str]=Field(description="Write top 5 keywords that truely represent review")
    advantages:List[str]=Field(description="write 3 advantages from review if available else write none")
    disadvantages:List[str]=Field(description="write 3 disadvantages from review if available else write none")
    name:str=Field(description="Write name of Author pf review")

structured=model.with_structured_output(review)

result=structured.invoke(""" I recently bought the SwiftRide X5, and overall I’m really happy with my decision. The car feels smooth to drive, and the handling is excellent even on rough roads. The fuel efficiency is impressive for a car in this segment, and the interiors are quite spacious and comfortable. The infotainment system is user-friendly, and I appreciate the modern safety features like lane assist and automatic braking.

On the downside, the boot space could have been a little larger, and the sound system is just average compared to competitors. Also, the plastic quality on some parts of the dashboard feels a bit cheap.

Despite these minor drawbacks, the SwiftRide X5 offers great value for money, especially for someone who wants a reliable daily driver with solid mileage and a premium feel. I would definitely recommend it to anyone looking for a practical yet stylish car.
review by: Hitesh Atkar""")

print(result)