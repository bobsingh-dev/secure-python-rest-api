import os
import secrets

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field

app = FastAPI(title="Secure REST API")

tasks= []

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
        )

class Task(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    completed: bool = False


def authenticate(api_key: str | None = Depends(api_key_header)):
    expected_key = os.getenv("API_KEY")

    if not expected_key:
        raise HTTPException(503, "Service unavailable")

    if not api_key or not secrets.compare_digest(
            api_key.encode(), expected_key.encode()
            ):
        raise HTTPException(401, "Invalid API key")



@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks", dependencies=[Depends(authenticate)])
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201, dependencies=[Depends(authenticate)])
def create_task(task: Task):
    tasks.append(task)
    return task
