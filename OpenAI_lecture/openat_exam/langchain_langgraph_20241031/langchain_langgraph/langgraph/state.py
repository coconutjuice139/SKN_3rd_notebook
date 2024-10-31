from typing import TypedDict, Annotated, List, Union
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import BaseMessage
import operator

# GraphState - 각 노드가 수행한 작업들을 기억(상태 기록)하는 기능
class AgentState(TypedDict):
   input: str
   chat_history: list[BaseMessage] # 대화 내용 중 '이전 메시지' 목록
   agent_outcome: Union[AgentAction, AgentFinish, None] # 유효한 유형으로 `None`이 필요
   intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]
