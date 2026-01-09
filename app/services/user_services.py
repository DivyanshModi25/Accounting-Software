from fastapi import HTTPException,Request,Depends
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.core.security import hash_password
from app.core.auth import verify_token

from app.db.models import User
from app.schemas.user_schema import UserCreate




def create_user(db:Session,data:UserCreate)->User:
    user = User(
        username = data.username,
        name = data.name,
        password_hash = hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user



def get_user_by_username(db:Session,username:str):
    return db.query(User).filter(User.username==username).first()



def get_current_user(request:Request,db:Session = Depends(get_db))->User:
    
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401,detail="Not authenticated")

    
    payload = verify_token(token)


    if not payload:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    

    user_id=payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401,detail="Invalid token payload")
    
    user = db.get(User,int(user_id))

    if not user:
        raise HTTPException(status_code=401,detail="User not found")
    
    return user


    
