## Simple CRUD Example with FastAPI

A simple example demonstrating the CRUD operations using **FastAPI**.

---

### Installation

```bash
pip install fastapi
```
### To run the app

```bash
fastapi dev simple.py
```
---

### Features

Create (POST) – Add a new item to the list
Read (GET) – Retrieve all items from the list
Update (PUT) – Update an existing item by its index
Delete (DELETE) – Remove an item by its index

---

### Swagger UI
Interactive API docs are available at:
```http://127.0.0.1:8000/docs```

### Endpoints

POST /items – Create item
GET /items – Read items
PUT /items/{item_id} – Update item at index
DELETE /items/{item_id} – Delete item at index