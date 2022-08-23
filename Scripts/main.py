import requests
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool


@app.get("/")
def read_root():
    url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json()}


@app.get("/items/{item_id}")
def fetch_root(item_id: int):
    url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items'
    response = requests.get(url+'/'+str(item_id), timeout=5)
    return {"item": response.json()}


@app.put("/itemsPut/{item_id}")
def update_item(item_id: int, item: Item):
    header = {'Content-type': 'application/json', 'Accept': 'Application/json'}
    url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items'
    requests.put(url+"/"+str(item_id), item.json(), headers=header)
    return "Se modifico correctamente"


@app.post("/itemsPost/")
def add_item(item: Item):
    header = {'Content-type': 'application/json', 'Accept': 'Application/json'}
    url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items'
    requests.post(url, item.json(), headers=header)
    return "Se agrego correctamente"


@app.delete("/delete/{item_id}")
def delet_item(item_id):
    url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items'
    requests.delete(url+"/"+str(item_id), timeout=5)
    return "Se borro correctamente"
