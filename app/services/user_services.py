from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user_schema import UserCreate,UserRead
from app.core.security import hash_password


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