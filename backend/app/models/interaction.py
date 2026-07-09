from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))

    interaction_type = Column(String)
    notes = Column(String)

    ai_summary = Column(String)
    next_action = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

