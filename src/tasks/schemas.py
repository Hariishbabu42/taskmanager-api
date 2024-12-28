# from pydantic import BaseModel
# from typing import Optional

# class TaskCreate(BaseModel):
#     title: str
#     description : str
#     completed: bool

# class TaskUpdate(BaseModel):
#     title: str
#     description : str
#     completed: bool

# class TaskStatusUpdate(BaseModel):
#     completed: bool

# class TaskResponse(BaseModel):
#     id: int
#     title : str
#     description: str
#     completed: bool
    
#     class Config:
#         from_attributes = True

from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool

class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool

class TaskStatusUpdate(BaseModel):
    completed: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)  # Updated for Pydantic 2.x
