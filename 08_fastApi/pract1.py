from fastapi import FastAPI
app= FastAPI()
@app.get("/product")
def get_user(limit: int=10):
    return {"limit": limit}

@app.get("/items")
def get_user(name: str=None, price: int=0):
    return {
        "name": name,
        "price": price
        }