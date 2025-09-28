from fastapi import APIRouter,Depends,HTTPException
from schemas.user import UserCreate ,UserLogin
from security import pass_hash,validate_password
from sqlalchemy.orm import Session
from database.db import engine,SessionLocal,get_db
from models.user import User as ModelUser

router=APIRouter(
    tags=['auth']
)

@router.post('/signup')
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    try:

        psw_hash=pass_hash(user.password)
        newUser=ModelUser(
            email=user.email,
            password_hash=psw_hash
        )
        print(newUser.__dict__)
        db.add(newUser)
        db.commit()
        return{'message':'todo correcto'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f'error: {e}')
    
@router.post('/login')
def login_user(user:UserLogin, db:Session=Depends(get_db)):
    db_user=db.query(ModelUser).filter(ModelUser.email==user.email).first()

    if not db_user:
        raise HTTPException(status_code=404,detail='usuario no encontrado')
    
    if not validate_password(user.password,db_user.password_hash):
        raise HTTPException(status_code=404,detail='contraseña incorrecta')
    
    return {
        "message": "bienvenido",
        "id": db_user.id,
        "email": db_user.email
    }