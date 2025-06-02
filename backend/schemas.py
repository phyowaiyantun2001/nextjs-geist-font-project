from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ----- System User Schemas -----
class SystemUserBase(BaseModel):
    username: str
    email: EmailStr

class SystemUserCreate(SystemUserBase):
    password: str

class SystemUserOut(SystemUserBase):
    id: int
    is_active: bool
    roles: List[str] = []

    class Config:
        orm_mode = True

# ----- Student Schemas -----
class StudentBase(BaseModel):
    full_name: str
    email: EmailStr

class StudentCreate(StudentBase):
    enroll_date: Optional[str] = None

class StudentOut(StudentBase):
    id: int
    enroll_date: Optional[str]

    class Config:
        orm_mode = True

# ----- Role and Permission Schemas -----
class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionOut(PermissionBase):
    id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    permissions: List[int]  # Permission IDs

class RoleOut(RoleBase):
    id: int
    permissions: List[PermissionOut] = []

    class Config:
        orm_mode = True

# ----- Authentication & Token Schemas -----
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
