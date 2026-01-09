from datetime import datetime,timedelta
from jose import jwt,JWTError
from app.core.config import PUBLIC_KEY,PRIVATE_KEY

ALGORITHM="RS256"
ACCESS_TOKEN_EXPIRY_MINUTES=60


def create_access_token(data:dict,expiry_minutes:int = ACCESS_TOKEN_EXPIRY_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expiry_minutes)
    to_encode.update({"exp":expire})

    token=jwt.encode(to_encode,PRIVATE_KEY,algorithm=ALGORITHM)
    return token



def verify_token(token:str):
    try:
        payload = jwt.decode(token,PUBLIC_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print("JWT ERROR:",e)
        return None