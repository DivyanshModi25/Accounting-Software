from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.user_schema import UserCreate,UserRead
from app.services.user_services import create_user


router = APIRouter(prefix='/users')



@router.post("/registerUser",response_model=UserRead)
def register_user(data:UserCreate, db:Session=Depends(get_db)):
    return create_user(db,data)






    