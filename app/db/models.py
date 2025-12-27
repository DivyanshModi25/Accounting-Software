from sqlalchemy import Column,Integer,String
from app.db.base import Base


class User(Base):
    __tablename__="Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    