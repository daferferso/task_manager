import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str


class TaskResponse(BaseModel):
    id: str
    name: str
    description: str


app = FastAPI()

@app.get("/")
def get_root():
    return "hello :s"


if __name__ == "__main__":
    uvicorn.run("main_api:app", host="127.0.0.1", port=8000, reload=True)
