from pydantic import BaseModel
from datetime import datetime


class InteractionCreate(BaseModel):
    hcp_id: int
    interaction_type: str
    notes: str


class InteractionResponse(BaseModel):
    id: int
    hcp_id: int
    interaction_type: str
    notes: str
    ai_summary: str | None = None
    next_action: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
