from pydantic import BaseModel
from typing import List, Optional

class ProfilesBase(BaseModel):
    nombre:str
    descripcion:Optional[str]=None
    distrito:Optional[str]=None
    ciudad:Optional[str]=None
    tarifa:Optional[float]=None
    foto_principal:Optional[str]=None
    galeria:Optional[List[str]]=None

class ProfilesCreate(ProfilesBase):
    user_id: int
    
class ProfilesUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    distrito: Optional[str] = None
    ciudad: Optional[str] = None
    tarifa: Optional[float] = None
    foto_principal: Optional[str] = None
    galeria: Optional[List[str]] = None



class ProfilePublic(ProfilesBase):
    id: int
    nombre: str
    # descripcion: Optional[str] 
    distrito: Optional[str]
    ciudad: Optional[str]
    tarifa: Optional[float]
    foto_principal: Optional[str]

    class Config:
        orm_mode = True