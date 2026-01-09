from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.auth.dependencies import get_current_user


from app.schemas.user_schema import UserCreate,UserReadProfile
from app.db.models.user_models import User

from app.services.user_services import create_user




router = APIRouter(prefix='/users')


@router.post("/registerUser",response_model=UserReadProfile)
def register_user(data:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,data)



@router.get("/me",response_model=UserReadProfile)
def current_user_profile(current_user:User = Depends(get_current_user)):
    return current_user


    