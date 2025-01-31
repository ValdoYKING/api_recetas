from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email:EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
