from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model=ChatPerplexity(model='sonar',temperature=0.5)

prompt=PromptTemplate(
    template="""write a notes from following paragraph \n {paragraph}""",
    input_variables=['paragraph']
)

prompt2=PromptTemplate(
    template="""Generate 5 FAQ from the given paragraph \n {paragraph}""",
    input_variables=['paragraph']
)

prompt3=PromptTemplate(
    template="""Merge the both input and give me conbined notes and FAQ \n notes= {notes} \n FAQ={faq}""",
    input_variables=['notes','faq']
)

parser=StrOutputParser()

pchain=RunnableParallel({
    'notes': prompt | model | parser,
    'faq': prompt2 | model | parser
})

mchain= prompt3 | model | parser
 
chain= pchain | mchain

paragraph="""Linear regression is one of the most fundamental and widely used statistical and machine learning techniques for modeling the relationship between a dependent variable (also called the target or response) and one or more independent variables (also called predictors or features). The main idea behind linear regression is to establish a linear relationship, meaning the target variable can be approximated as a straight-line function of the input variables. In the simplest case, known as simple linear regression, there is only one independent variable, and the relationship is modeled as y = \beta_0 + \beta_1x + \epsilon, where y is the dependent variable, x is the independent variable, \beta_0 is the intercept, \beta_1 is the slope or coefficient that represents the change in y for a one-unit change in x, and \epsilon is the error term accounting for variability not captured by the model. In multiple linear regression, more than one independent variable is used, and the model becomes y = \beta_0 + \beta_1x_1 + \beta_2x_2 + … + \beta_nx_n + \epsilon. The coefficients (\beta) are usually estimated using the method of least squares, which minimizes the sum of squared differences between the observed values and the values predicted by the model. Linear regression is valued for its simplicity, interpretability, and efficiency, making it a strong baseline model in predictive analytics. However, it assumes linearity between variables, independence of errors, homoscedasticity (constant variance of errors), and normally distributed errors. If these assumptions are violated, the model’s accuracy and reliability may suffer. Despite its limitations, linear regression remains an essential tool in data analysis, finance, economics, and machine learning applications, providing insights into relationships among variables and serving as a foundation for more advanced models."""

result=chain.invoke(paragraph)

print(result)

chain.get_graph().print_ascii()