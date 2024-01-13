from langchain_openai import ChatOpenAI 
from langchain_openai import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chains import LLMChain, LLMMathChain, ConversationChain
from langchain.prompts import PromptTemplate
from langchain_community.tools import wikipedia
import math 

template = """Question: {question}
Let's think step by step.
Answer: """
prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = """ What is the population of the capital of the country where the
Olympic Games were held in 2016? """
llm_chain.invoke(question)


tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

question = """What is the square root of the population of the capital of the
country where the Olympic Games were held in 2016 ?"""
agent.invoke(question)

