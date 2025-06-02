from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import RoleCreate, RoleOut
from crud import create_role
from database import get_db

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", response_model=RoleOut)
def add_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)
