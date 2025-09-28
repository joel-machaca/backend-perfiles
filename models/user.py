from database.db import Base
from sqlalchemy import Column,Integer,String,Float,Text,ForeignKey,TIMESTAMP,func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    email=Column(String(100),unique=True,nullable=False)
    password_hash=Column(String(200) ,nullable=False)
    registration_date=Column(TIMESTAMP,server_default=func.now())

    profile=relationship('Profiles', back_populates='owner')
