from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email:EmailStr
    password:str

class UserCreate(UserBase):
    pass

class UserLogin(UserBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    registration_date:str

    # class Config:
    #     orm_mode=True