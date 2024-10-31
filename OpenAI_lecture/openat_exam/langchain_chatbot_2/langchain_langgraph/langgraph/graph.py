##      Define the graph
from langgraph.graph import END, StateGraph
from langchain_langgraph.langgraph.state import AgentState
from langchain_langgraph.langgraph.nodes import run_agent, execute_tools, should_continue

# lang-graph structure
def create_graph_structure():
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", run_agent)
    workflow.add_node("action", execute_tools)
    workflow.set_entry_point("agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "action",
            "end": END
        }
    )
    workflow.add_edge('action', 'agent')
    return workflow

# app
def set_workflow_to_app():   # really this is the graph.
    return create_graph_structure().compile()    # to be like an app in here