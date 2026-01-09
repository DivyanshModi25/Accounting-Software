from fastapi import Request,Depends,HTTPException
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.auth.jwt import verify_token


from app.db.models import User



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


    
