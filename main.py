from typing import Union
from fastapi import FastAPI, Request

app = FastAPI()

data = {}

@app.get("/") 
def read_root():
    return data

@app.post("/")
async def post_root(request: Request):
    pre = await request.json()
    data[pre.get('nim')] = pre.get('nama')
    return data