from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email:EmailStr
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
