from passlib.context import CryptContext

pass_context=CryptContext(schemes=["bcrypt"])

def pass_hash(password:str) -> str:
    return pass_context.hash(password)

def validate_password(password_normal:str,password_hash:str) ->bool:
    return pass_context.verify(password_normal,password_hash)