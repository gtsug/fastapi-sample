from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: Todo):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = todo
    return todo

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos.pop(todo_id)


