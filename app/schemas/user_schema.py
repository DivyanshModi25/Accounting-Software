from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password:str
    name:str 


class UserReadProfile(BaseModel):
    id:int 
    name:str
    username:str

    class config:
        from_attributes=True


