from typing import TypedDict
from langgraph.graph import StateGraph, END

from app.services.groq_service import ask_llm


class CRMState(TypedDict):
    question: str
    answer: str


def ai_node(state: CRMState):
    response = ask_llm(state["question"])

    return {
        "answer": response
    }


workflow = StateGraph(CRMState)

workflow.add_node("ai_node", ai_node)

workflow.set_entry_point("ai_node")

workflow.add_edge("ai_node", END)

graph = workflow.compile()