from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Enable CORS (replace "*" with the frontend URL in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your API endpoints go here...


class User(BaseModel):
    name: str
    age: int
    sex: str
    designation: str
    address: str
    phone: str
    bloodgroup: str
    department: str


# SQLite3 connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Table creation query
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        sex TEXT NOT NULL,
        designation TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL,
        bloodgroup TEXT NOT NULL,
        department TEXT NOT NULL
    )
"""

# Execute the table creation query
cursor.execute(create_table_query)

# API endpoints


@app.post("/users/", response_model=User)
async def create_user(user: User):
    try:
        cursor.execute(
            "INSERT INTO users (name, age, sex, designation, address, phone, bloodgroup, department) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user.name, user.age, user.sex, user.designation,
             user.address, user.phone, user.bloodgroup, user.department)
        )
        conn.commit()
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/users/", response_model=List[User])
async def get_users():
    try:
        cursor.execute(
            "SELECT name, age, sex, designation, address, phone, bloodgroup, department FROM users")
        users_data = cursor.fetchall()
        users = [
            User(
                name=row[0],
                age=row[1],
                sex=row[2],
                designation=row[3],
                address=row[4],
                phone=row[5],
                bloodgroup=row[6],
                department=row[7]
            )
            for row in users_data
        ]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Close the connection after the server stops


@app.on_event("shutdown")
def shutdown_event():
    conn.close()
