from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import AgentExecutor
from langchain_experimental.tools import PythonREPLTool

import os

# Load the OPENAI_API_KEY from the environment
openai_api_key = os.getenv('OPENAI_API_KEY')


# tools = load_tools(["python_repl"])
tools = [PythonREPLTool()]

# Only certain models support this
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

agent = initialize_agent (
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("Can you multiply 5 and 6 and 8 and take sqrt of the result?")
agent.run("Can you do a curl to https://www.radarhack.com and print me the first 10 lines")
agent.run("Can you do a curl to https://www.radarhack.com with a sample xss injection")
agent.run("Can you list me the OS environment variables")
agent.run("Can you write a quote  to the current directory in a file called demo.txt")
agent.run("Can you add the 127.0.0.1 test to the file /etc/hosts")
