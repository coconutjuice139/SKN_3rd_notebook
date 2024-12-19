from langchain.agents import create_openai_functions_agent
from langchain_exaone_api.model import creat_chat_model
from langchain_exaone_api.langgraph.tools import get_langgraph_tools
from langchain_exaone_api.prompt import pull_langgraph_prompt, create_prompt
from langchain.agents import initialize_agent, Tool
from langchain.prompts.chat import ChatPromptTemplate
from langchain_exaone_api.model import FastAPILLM
from langchain.prompts import PromptTemplate
# # agent_runnable
# def create_openai_langgraph_agent():
#     llm = llm
#     tools = get_langgraph_tools(),
#     prompt = create_prompt()
#     return create_openai_functions_agent(llm, tools, prompt) # 이게 agent-scratchpad를 필요로 하는 함수여서 프롬프트에 agent-scratchpad가 무조건 들어가야 함


# FastAPI 서버 URL
FASTAPI_URL = "https://backdocsend.jamesmoon.click/exaone/generate"

# FastAPI LLM Wrapper
fastapi_llm = FastAPILLM(api_url=FASTAPI_URL, model_name="exaone3.5")

# LangChain Agent 설정
tools = [
    Tool(
        name="Example Tool",
        func=lambda x: f"Tool received: {x}",
        description="Example tool for processing input"
    )
]

import logging
logging.basicConfig(level=logging.DEBUG)

# def create_openai_langgraph_agent():
#     logging.debug("Creating LangChain agent...")
#     logging.debug(f"Tools: {tools}")
#     logging.debug(f"LLM: {fastapi_llm}")

#     agent = initialize_agent(
#         tools=tools,
#         llm=fastapi_llm,
#         agent="zero-shot-react-description",
#         verbose=True,
#     )

#     logging.debug(f"Agent created: {agent}")
    # return agent

def create_openai_langgraph_agent():
    logging.debug("Creating LangChain agent...")
    logging.debug(f"Tools: {tools}")
    logging.debug(f"LLM: {fastapi_llm}")
    
    prompt = PromptTemplate(
        input_variables=["input", "intermediate_steps"],
        template=(
            "Answer the following questions as best you can. You have access to the following tools:\n\n"
            "Example Tool(x) - Example tool for processing input\n\n"
            "Use the following format:\n\n"
            "Question: {input}\n"
            "Thought: let me approach this step by step\n"
            "Action: the action to take, should be one of [Example Tool]\n"
            "Action Input: the input to the action\n"
            "Observation: the result of the action\n"
            "... (this Thought/Action/Action Input/Observation can repeat N times)\n"
            "Thought: I now know the final answer\n"
            "Final Answer: the final answer to the original input question\n\n"
            "Previous steps: {intermediate_steps}\n"
        )
    )

    agent = initialize_agent(
        tools=tools,
        llm=fastapi_llm,
        agent="zero-shot-react-description",
        verbose=True,
        agent_kwargs={
            "prefix": prompt.template
        }
    )

    return agent