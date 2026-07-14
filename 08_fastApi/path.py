#path + query + body combo
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []
class User(BaseModel):
    user_id:int
    name:str
    age:int
@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":"user created",
        "data":user
    }      

@app.put("/users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool=False):
    if user_id<len(users):
        users[user_id]=user 
        return{
            "message":"user updated",
            "notify":notify,
            "data":user
        }
    return{
        "error":"user not found"
    }
@app.get("/user/{user_id}")
def get_user(user_id: int):  #read
    for user in users:
        if user.user_id == user_id:
            return user
    return {"error": "user not found"}