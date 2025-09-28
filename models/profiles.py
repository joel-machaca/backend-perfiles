from database.db import Base
from sqlalchemy import Column,Integer,String,Float,Text,ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

class Profiles(Base):
    __tablename__='profiles'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'),unique=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    distrito = Column(String(50))
    ciudad = Column(String(50))
    tarifa = Column(Float)
    foto_principal = Column(String(250))
    galeria = Column(JSON)

    owner=relationship('User',back_populates='profile')
