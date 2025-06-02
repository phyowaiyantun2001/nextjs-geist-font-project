from sqlalchemy.orm import Session
from models import SystemUser, Student, Role, Permission
from schemas import SystemUserCreate
from auth import get_password_hash

def get_user_by_username(db: Session, username: str):
    return db.query(SystemUser).filter(SystemUser.username == username).first()

def create_system_user(db: Session, user_in: SystemUserCreate):
    hashed_password = get_password_hash(user_in.password)
    db_user = SystemUser(username=user_in.username, email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_student(db: Session, student_data):
    db_student = Student(**student_data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_role(db: Session, role_in):
    db_role = Role(name=role_in.name, description=role_in.description)
    # assign permissions if provided
    if role_in.permissions:
        db_role.permissions = db.query(Permission).filter(Permission.id.in_(role_in.permissions)).all()
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def assign_role_to_user(db: Session, user: SystemUser, role: Role):
    user.roles.append(role)
    db.commit()
    db.refresh(user)
    return user
