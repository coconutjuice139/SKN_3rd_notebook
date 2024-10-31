from langchain.agents import create_openai_functions_agent
from langchain_langgraph.model import creat_chat_model
from langchain_langgraph.langgraph.tools import get_langgraph_tools
from langchain_langgraph.prompt import pull_langgraph_prompt

# agent_runnable
def create_openai_langgraph_agent():
    llm = creat_chat_model(model_id="gpt-4o-mini", streaming=True)
    tools = get_langgraph_tools()
    prompt = pull_langgraph_prompt()
    return create_openai_functions_agent(llm, tools, prompt)

# inputs = {"input": "give me a random number and then write in words",
#           "chat_history": [],
#           "intermediate_steps":[]}

# agent_runnable = create_openai_langgraph_agent()

# agent_outcome = agent_runnable.invoke(inputs)