from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import validator

class TodoBase(SQLModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = Field(default=False)

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

class TodoUpdate(SQLModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None
    
    @validator('title')
    def title_cannot_be_empty(cls, v):
        if v is not None and len(v.strip()) == 0:
            raise ValueError('Title cannot be empty')
        return v