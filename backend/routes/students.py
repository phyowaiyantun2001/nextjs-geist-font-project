from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import StudentCreate, StudentOut
from crud import create_student
from models import Student

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentOut)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Add any student-specific validation as required.
    return create_student(db, student)

@router.get("/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
