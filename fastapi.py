from typing import ItemsView, Optional
from fastapi import FastAPI
from fastapi.params import Path, Query
from pydantic import BaseModel
app = FastAPI()

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:float=None
    brand:Optional[str]=None
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str] =None
@app.get("/")
def home():
    return {"Data":"Testinggggg"}
    
@app.get("/about")
def about():
    return {"Data":"About"}

inventory = {
    1:{
        "name":"Milk",
        "price":4,
        "brand":"Regular"
      }
   }

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to see")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str=Query(None, title="Name",description="The name of the item you would like to see")):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
        else:
            return {"Data": "Not found"}
@app.post("/create-item/{item_id}")
def create_item(item_id:int, item: Item):
    if item_id in inventory:
        return{"Error": "Item ID already exists."}

    inventory[item_id] = item
    return inventory[item_id]
    
@app.put("/update-item/{item_id}")
def update_item(item_id:int, item:UpdateItem):
    if item_id not in inventory:
        return {"Error":"Item ID does not exist"}
    
    if item.name!=None:
        inventory[item_id].name=item.name

    if item.price!=None:
        inventory[item_id].price=item.price

    if item.brand!=None:
        inventory[item_id].brand=item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int=Query(...,description="The ID of the item to be deleted")):
    if item_id not in inventory:
        return {"Error":"ID does not exist."}
    del inventory[item_id]
    return {"Success":'item deleted!'}
