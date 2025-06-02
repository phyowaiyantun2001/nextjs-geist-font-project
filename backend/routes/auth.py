from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import SystemUserCreate, Token
from crud import get_user_by_username, create_system_user
from database import get_db
from auth import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=dict)
def register(user_in: SystemUserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user = create_system_user(db, user_in)
    return {"msg": "User registered successfully", "user_id": user.id}

@router.post("/login", response_model=Token)
def login(user_in: SystemUserCreate, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_in.username)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
