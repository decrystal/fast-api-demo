from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


def index(age):
    return {"fun": "/index", "age": age}


# 这里data不能用data=Login, 因为它是一个json, 要用:

def login(data: Login):
    return {"fun": data}
