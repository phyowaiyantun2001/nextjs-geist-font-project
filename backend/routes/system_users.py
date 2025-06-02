from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_current_user
from database import get_db
from schemas import SystemUserOut
from models import SystemUser

router = APIRouter(prefix="/system-users", tags=["system-users"])

@router.get("/", response_model=list[SystemUserOut])
def list_system_users(db: Session = Depends(get_db), current_user: SystemUser = Depends(get_current_user)):
    # Authorization: current_user must have high-level role (not detailed here)
    return db.query(SystemUser).all()

@router.get("/{user_id}", response_model=SystemUserOut)
def get_system_user(user_id: int, db: Session = Depends(get_db), current_user: SystemUser = Depends(get_current_user)):
    user = db.query(SystemUser).filter(SystemUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
