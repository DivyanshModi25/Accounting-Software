from fastapi import APIRouter,Depends,Request
from sqlalchemy.orm import Session


from app.db.session import get_db


from app.schemas.user_schema import UserCreate,UserReadProfile


from app.services.user_services import create_user
from app.auth.dependencies import get_current_user





router = APIRouter(prefix='/users')


@router.post("/registerUser",response_model=UserReadProfile)
def register_user(data:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,data)



@router.post("/me",response_model=UserReadProfile)
def current_user_profile(request:Request,db:Session=Depends(get_db)):
    user_profile = get_current_user(request,db)

    return user_profile


    