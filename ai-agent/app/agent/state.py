from typing import TypedDict

class AgentState(TypedDict):
    query: str
    context: str
    insight: str
    relevant: bool
    retry_count: int