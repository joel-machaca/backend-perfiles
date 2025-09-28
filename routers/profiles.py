from fastapi import APIRouter,Depends,HTTPException,UploadFile,File,Form
from typing import List
from sqlalchemy.orm import Session
from schemas.profiles import ProfilePublic,ProfilesUpdate
from database.db import get_db
from models.profiles import Profiles as ModelProfiles
from dotenv import load_dotenv
from supabase import create_client
import os


router=APIRouter(
    prefix='/profiles',
    tags=['profiles']
)
load_dotenv()

SUPABASE_URL = "https://dswakzcxymsbalttunzq.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") 
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/create")
def create_profiles(
    user_id: int = Form(...),
    nombre: str = Form(...),
    descripcion: str = Form(...),
    distrito: str = Form(...),
    ciudad: str = Form(...),
    tarifa: float = Form(...),
    foto_principal: UploadFile = File(...),
    galeria: List[UploadFile] = File([]),
    db: Session = Depends(get_db)
):
    # Subir foto principal a Supabase
    principal_data = foto_principal.file.read()
    supabase.storage.from_('uploads').upload(foto_principal.filename, principal_data)
    foto_url = supabase.storage.from_('uploads').get_public_url(foto_principal.filename)

    # Subir galería
    galeria_urls = []
    for img in galeria:
        data = img.file.read()
        supabase.storage.from_('uploads').upload(img.filename, data)
        galeria_urls.append(supabase.storage.from_('uploads').get_public_url(img.filename))

    newProfile = ModelProfiles(
        user_id=user_id,
        nombre=nombre,
        descripcion=descripcion,
        distrito=distrito,
        ciudad=ciudad,
        tarifa=tarifa,
        foto_principal=foto_url,
        galeria=galeria_urls
    )

    db.add(newProfile)
    db.commit()
    db.refresh(newProfile)
    return newProfile

@router.get('/all',response_model=List[ProfilePublic])
def get_profiles(db: Session = Depends(get_db)):
    profiles=db.query(ModelProfiles).all()
    return profiles

@router.put('/me',response_model=ProfilePublic)
def update(user_id:int, user:ProfilesUpdate,db:Session=Depends(get_db)):
    profile=db.query(ModelProfiles).filter(ModelProfiles.user_id == user_id).first()

    if not profile:
        raise HTTPException(status_code=404,detail='perfil no encontrado')
    
    update_data=user.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(profile,key,value)
    db.commit()
    return profile

@router.get('/me',response_model=ProfilePublic)
def get_my_profile(user_id:int,db:Session=Depends(get_db)):
    profile=db.query(ModelProfiles).filter(ModelProfiles.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404,detail='perfil no encontrado')
    return profile

@router.get('/me/{profile_id}',response_model=ProfilePublic)
def get_profile_public(profile_id:int,db:Session=Depends(get_db)):
    profile=db.query(ModelProfiles).filter(ModelProfiles.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404,detail='perfil no encontrado')
    return profile