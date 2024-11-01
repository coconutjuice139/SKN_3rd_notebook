from langchain_core.agents import AgentFinish
from langgraph.prebuilt.tool_executor import ToolExecutor
from langchain_memory_common.langgraph.tools import get_langgraph_tools 
from langchain_memory_common.langgraph.agent import create_openai_langgraph_agent
from langchain_core.messages import trim_messages, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_memory_common.model import creat_chat_model
from langchain_memory_common.langgraph.state import AgentState

# trimmer
def set_trimmer():
    return trim_messages(strategy="last", max_tokens=5, token_counter=len)

# Define the function that calls the model
def call_model(state:AgentState): # data 이거 집어넣어야 함##################################################
    print(state)
    # 필요 시 메시지를 트리밍 (생략 가능)
    trimmed_messages = set_trimmer().invoke(state['input'], state["agent_outcome"].return_values['output'])
    print("--------------")
    print(trimmed_messages)
    # 시스템 프롬프트와 메시지 설정
    messages = [SystemMessage(content="You are a helpful assistant. Answer all questions to the best of your ability.")] + trimmed_messages
    # 모델 호출
    state['chat_history'].append(messages)
    return state

# agent llm을 만드는 함수
def run_agent(data):
    agent_outcome = create_openai_langgraph_agent().invoke(data)
    return {"agent_outcome": agent_outcome}

# tools 생성 함수
def execute_tools(data):
    agent_action = data['agent_outcome']
    output = ToolExecutor(get_langgraph_tools()).invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}

# 메세지 분기
def should_continue(data):
    # AgentFinish는 사용자에게 다시 보낼 최종 메시지가 포함된 응답입니다.
    # 이 응답은 에이전트 실행을 종료하는데 사용되어야 합니다.
    if isinstance(data['agent_outcome'], AgentFinish):
        return "end"
    else:
        return "continue"