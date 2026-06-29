from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "this is bout page"}

@app.get("/users")
def users():
    return {"users":['afnan','saif','ammar','fawaz']}

