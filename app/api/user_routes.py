from fastapi import APIRouter,Depends,HTTPException, Response

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_password
from app.core.auth import create_access_token

from app.schemas.user_schema import UserCreate,UserRead
from app.schemas.auth_schema import LoginRequest
from app.services.user_services import create_user,get_user_by_username


router = APIRouter(prefix='/users')



@router.post("/registerUser",response_model=UserRead)
def register_user(data:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,data)



@router.post("/login")
def login_user(data:LoginRequest,response:Response,db:Session = Depends(get_db)):
    
    user = get_user_by_username(db,data.username)

    if not user or not verify_password(data.password,user.password_hash):
        raise HTTPException(status_code=401,detail="Invalid credentials")
     
    token = create_access_token({
        "sub":str(user.id)
    })

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60*30,
        path="/"
    )


    return {"message":"User logged in successfully"}

    