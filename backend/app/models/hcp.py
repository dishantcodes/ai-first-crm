from sqlalchemy import Column, Integer, String
from app.database.database import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    hospital = Column(String, nullable=False)
    city = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)