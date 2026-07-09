from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.crm_graph import graph


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat_ai(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "answer": ""
        }
    )

    return {
        "answer": result["answer"]
    }


@router.get("/test")
def test_ai():

    result = graph.invoke(
        {
            "question": "Explain AI CRM in one sentence.",
            "answer": ""
        }
    )

    return result
