### FastAPI CRUD Examples

This folder contains two simple CRUD examples built with **FastAPI**.

---

#### 1. simple.py
CRUD using an in-memory Python list.  
- No database, just a Python list to store items.  
- Endpoints: Create, Read, Update, Delete.  

Run:
```bash
fastapi dev simple.py
```

--- 

#### 2. orm_db.py
CRUD using SQLAlchemy with SQLite database.

- Demonstrates ORM (Object Relational Mapping).
- Items are stored in a real database table.

Run:
```bash
fastapi dev orm_db.py
```

---

#### Swagger UI

Interactive API docs (for both examples) are available at:
http://127.0.0.1:8000/docs