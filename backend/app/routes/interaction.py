from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate, InteractionResponse
from app.graph.crm_graph import graph


router = APIRouter(
    prefix="/interaction",
    tags=["Interaction"]
)


@router.post("/", response_model=InteractionResponse)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):

    # AI Summary generate
    result = graph.invoke(
        {
            "question": interaction.notes,
            "answer": ""
        }
    )

    ai_response = result["answer"]


    new_interaction = Interaction(
        hcp_id=interaction.hcp_id,
        interaction_type=interaction.interaction_type,
        notes=interaction.notes,
        ai_summary=ai_response,
        next_action="Follow up with doctor"
    )


    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction



@router.get("/", response_model=list[InteractionResponse])
def get_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()
