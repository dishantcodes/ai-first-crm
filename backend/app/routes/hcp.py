from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database.database import get_db
from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate, HCPResponse

router = APIRouter(
    prefix="/hcp",
    tags=["HCP"]
)


@router.post("/", response_model=HCPResponse)
def create_hcp(hcp: HCPCreate, db: Session = Depends(get_db)):
    new_hcp = HCP(**hcp.model_dump())

    db.add(new_hcp)
    db.commit()
    db.refresh(new_hcp)

    return new_hcp


@router.get("/", response_model=list[HCPResponse])
def get_all_hcp(db: Session = Depends(get_db)):
    return db.query(HCP).all()


# SEARCH API (pehle rakha hai)
@router.get("/search")
def search_hcp(query: str, db: Session = Depends(get_db)):

    return db.query(HCP).filter(
        or_(
            HCP.name.ilike(f"%{query}%"),
            HCP.speciality.ilike(f"%{query}%"),
            HCP.city.ilike(f"%{query}%")
        )
    ).all()


@router.get("/{hcp_id}", response_model=HCPResponse)
def get_hcp(hcp_id: int, db: Session = Depends(get_db)):

    hcp = db.query(HCP).filter(HCP.id == hcp_id).first()

    if not hcp:
        raise HTTPException(status_code=404, detail="HCP not found")

    return hcp


@router.put("/{hcp_id}", response_model=HCPResponse)
def update_hcp(
    hcp_id: int,
    hcp_data: HCPCreate,
    db: Session = Depends(get_db)
):

    hcp = db.query(HCP).filter(HCP.id == hcp_id).first()

    if not hcp:
        raise HTTPException(status_code=404, detail="HCP not found")

    for key, value in hcp_data.model_dump().items():
        setattr(hcp, key, value)

    db.commit()
    db.refresh(hcp)

    return hcp


@router.delete("/{hcp_id}")
def delete_hcp(hcp_id: int, db: Session = Depends(get_db)):

    hcp = db.query(HCP).filter(HCP.id == hcp_id).first()

    if not hcp:
        raise HTTPException(status_code=404, detail="HCP not found")

    db.delete(hcp)
    db.commit()

    return {"message": "HCP deleted successfully"}
