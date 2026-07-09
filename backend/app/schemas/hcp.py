from pydantic import BaseModel, EmailStr


class HCPCreate(BaseModel):
    name: str
    specialization: str
    hospital: str
    city: str
    email: EmailStr
    phone: str


class HCPResponse(HCPCreate):
    id: int

    class Config:
        from_attributes = True