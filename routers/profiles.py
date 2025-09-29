from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from typing import List
from sqlalchemy.orm import Session
from schemas.profiles import ProfilePublic, ProfilesUpdate
from database.db import get_db
from models.profiles import Profiles as ModelProfiles
from dotenv import load_dotenv
from supabase import create_client
import os

router = APIRouter(
    prefix='/profiles',
    tags=['profiles']
)
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
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
    try:
        principal_data = foto_principal.file.read()
        path = f"user_{user_id}/{foto_principal.filename}"

        
        try:
            supabase.storage.from_('uploads').remove([path])
        except Exception:
            pass

        supabase.storage.from_('uploads').upload(path, principal_data)
        foto_url = supabase.storage.from_('uploads').get_public_url(path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error subiendo foto principal: {e}")

    galeria_urls = []
    for img in galeria:
        data = img.file.read()
        path = f"user_{user_id}/{img.filename}"

        try:
            supabase.storage.from_('uploads').remove([path])
        except Exception:
            pass

        supabase.storage.from_('uploads').upload(path, data)
        galeria_urls.append(supabase.storage.from_('uploads').get_public_url(path))

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


@router.get('/all', response_model=List[ProfilePublic])
def get_profiles(db: Session = Depends(get_db)):
    profiles = db.query(ModelProfiles).all()
    return profiles


@router.put("/me", response_model=ProfilePublic)
def update_profile(
    user_id: int = Form(...),
    nombre: str = Form(None),
    descripcion: str = Form(None),
    distrito: str = Form(None),
    ciudad: str = Form(None),
    tarifa: float = Form(None),
    foto_principal: UploadFile = File(None),
    galeria: List[UploadFile] = File([]),
    db: Session = Depends(get_db),
):
    profile = db.query(ModelProfiles).filter(ModelProfiles.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="perfil no encontrado")

    if nombre: profile.nombre = nombre
    if descripcion: profile.descripcion = descripcion
    if distrito: profile.distrito = distrito
    if ciudad: profile.ciudad = ciudad
    if tarifa: profile.tarifa = tarifa

    if foto_principal:
        data = foto_principal.file.read()
        path = f"user_{user_id}/{foto_principal.filename}"

        try:
            supabase.storage.from_("uploads").remove([path])
        except Exception:
            pass

        supabase.storage.from_("uploads").upload(path, data)
        profile.foto_principal = supabase.storage.from_("uploads").get_public_url(path)

    if galeria:
        urls = []
        for img in galeria:
            data = img.file.read()
            path = f"user_{user_id}/{img.filename}"

            try:
                supabase.storage.from_("uploads").remove([path])
            except Exception:
                pass

            supabase.storage.from_("uploads").upload(path, data)
            urls.append(supabase.storage.from_("uploads").get_public_url(path))
        profile.galeria = urls

    db.commit()
    db.refresh(profile)
    return profile



@router.get('/me', response_model=ProfilePublic)
def get_my_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(ModelProfiles).filter(ModelProfiles.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail='perfil no encontrado')
    return profile



@router.get('/me/{profile_id}', response_model=ProfilePublic)
def get_profile_public(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(ModelProfiles).filter(ModelProfiles.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail='perfil no encontrado')
    return profile
