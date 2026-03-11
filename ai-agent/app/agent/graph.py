from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import search_node, analyst_node, check_relevance_node
from app.core.config import settings

workflow = StateGraph(AgentState)

workflow.add_node("searcher", search_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("checker", check_relevance_node)

workflow.set_entry_point("searcher")
workflow.add_edge("searcher", "analyst")
workflow.add_edge("analyst", "checker")

def decide_to_finish(state: AgentState):
    if state["relevant"] or state["retry_count"] >= settings.MAX_RETRIES:
        return END
    return "searcher"

workflow.add_conditional_edges("checker", decide_to_finish)
app_graph = workflow.compile()