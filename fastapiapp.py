from fastapi import FastAPI,Path,Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None

students={
    1:{
        "name":"sujan",
        "age":25,
        "class":"year 12"
    }
}

inventory={}

@app.get("/")
def index():
    return{"name":"first data"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None,description="Please enter the appropriate number",gt=0)):
    return students[student_id] 


@app.get("/get-by-name")
def get_item(item_id:int=Path(None,description="Name of Item")):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
    raise HTTPException(status_code=404,detail="Item Name not found")

@app.get("/get-item/{item_id}/{name}")
def get_item(item_id:int,name:str):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*,item_id:int,name:Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id].name==name:
            return inventory[item_id]
        return{"Data":"Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return{"error":"Item id already exists"}
    
    inventory[item_id]=item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        return{"error":"Item id doesn't  exists"}
    
    if item.name !=None:
        inventory[item_id].name=item.name
    if item.price !=None:
        inventory[item_id].price=item.price
    if item.brand !=None:
        inventory[item_id].brand=item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int=Query(..., description="The id of the item is about to delete ")):
    if item_id not in inventory:
        return {"Error":"Id does not exist"}

    del inventory[item_id]
    return{"sucess":"Item deleted!"}
