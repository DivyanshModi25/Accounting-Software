from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")
# or we can directly use  argon2-cffi



def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(password:str,hashedPass:str) -> bool:
    return pwd_context.verify(password,hashedPass)

