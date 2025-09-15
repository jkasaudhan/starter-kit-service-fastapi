from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.db.session import get_session
from app.models.todo import Todo, TodoCreate, TodoUpdate, TodoRead

api_router = APIRouter()

@api_router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

@api_router.get("/todos", response_model=List[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@api_router.get("/todos/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@api_router.post("/todos", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@api_router.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate, session: Session = Depends(get_session)):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@api_router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    session.delete(todo)
    session.commit()
    return