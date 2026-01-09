from sqlalchemy import Integer,String
from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column


class User(Base):
    __tablename__="Users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String, nullable=False)
    username:Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash:Mapped[str] = mapped_column(String, nullable=False)