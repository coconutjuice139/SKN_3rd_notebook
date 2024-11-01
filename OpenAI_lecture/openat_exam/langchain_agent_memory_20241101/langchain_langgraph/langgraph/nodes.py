from langchain_core.agents import AgentFinish
from langgraph.prebuilt.tool_executor import ToolExecutor
from langchain_langgraph.langgraph.tools import get_langgraph_tools 
from langchain_langgraph.langgraph.agent import create_openai_langgraph_agent


def run_agent(data):
    agent_outcome = create_openai_langgraph_agent().invoke(data)
    return {"agent_outcome": agent_outcome}

def execute_tools(data):
    agent_action = data['agent_outcome']
    output = ToolExecutor(get_langgraph_tools()).invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}

def should_continue(data):
    # AgentFinish는 사용자에게 다시 보낼 최종 메시지가 포함된 응답입니다.
    # 이 응답은 에이전트 실행을 종료하는데 사용되어야 합니다.
    if isinstance(data['agent_outcome'], AgentFinish):
        return "end"
    else:
        return "continue"