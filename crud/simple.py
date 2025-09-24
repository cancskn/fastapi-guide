from typing import Any
from fastapi import FastAPI

app = FastAPI()

# list to store items
items = []

# Create
@app.post("/items")
def create_items(item: Any):
    items.append(item)
    return {"message": "Item added", "item": item}

# Read
@app.get("/items")
def read_items():
    return {"items": items}

# Update
@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: Any):
    items[item_id] = new_item
    return {"message": "Item updated", "item": new_item}

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted}


# Test

# add any type
# items.append('Book')
# items.append({'id':1, "name": 'Laptop'})
# items.append(100)

# # update an item
# items[0] = 'Pen'

# # delete an item
# deleted = items.pop(1)
# print("deleted:", deleted)