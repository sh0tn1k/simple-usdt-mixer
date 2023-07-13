from pydantic import BaseModel

class UserCreate(BaseModel):
    login : str
    username : str
    password : str

class ShowUser(BaseModel):
    username : str 
    login : str
    password : str

    class Config(): #приказывает pydantic преобразовывать даже недиктованные объекты в json
        orm_mode = True