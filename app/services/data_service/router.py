from fastapi import APIRouter
from .models import Item

router = APIRouter()

# In-memory storage for demonstration purposes
items = {}

@router.post("/items/", response_model=Item, operation_id="createItem")
async def create_item(item: Item):
    items[item.id] = item
    return item

@router.get("/items/{item_id}", response_model=Item, operation_id="readItem")
async def read_item(item_id: int):
    return items.get(item_id)

@router.put("/items/{item_id}", response_model=Item, operation_id="updateItem")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@router.delete("/items/{item_id}", operation_id="deleteItem")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted"}