from typing import List  # Import the List type
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


class User(BaseModel):
    name: str
    age: int
    sex: str
    designation: str
    address: str
    phone: str
    bloodgroup: str
    department: str


fake_users_db = []


@app.post("/users/", response_model=User)
async def create_user(user: User):
    fake_users_db.append(user)
    return user


# Use List[User] instead of list[User]
@app.get("/users/", response_model=List[User])
async def get_users():
    return fake_users_db
