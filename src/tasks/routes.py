import os
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.tasks.models import Task
from src.core.logging import logger
from src.tasks.schemas import TaskCreate, TaskResponse, TaskUpdate, TaskStatusUpdate
from src.tasks.crud import db_operations
from src.core.database import get_db

router =  APIRouter(prefix="/tasks", tags =['Tasks'])


@router.get("/")
async def read_root():
    try:
        return {"message" : "welcome"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/create_task", response_model=TaskResponse)
async def create_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db)):
    try:
        maximum_id = await db_operations.get_max_task_id(db)
        new_id = (maximum_id + 1) if maximum_id else 1
        task_data_dict = task_data.dict()
        task_data_dict['id'] = new_id
        task = await db_operations.create_task(db, task_data_dict)
        if not task:
            logger.error("Error while creating task: Task not found")
            raise HTTPException(status_code=404, detail="Task not found")
        logger.info("Task created successfully")
        return task
    except Exception as e:
        logger.exception("An unexpected error occurred while creating a task")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/all", response_model=List[TaskResponse])
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    try:
        task = await db_operations.get_tasks(db)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        logger.exception("An unexpected error occurred while getting all tasks")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/{task_id}", response_model= TaskResponse)
async def get_task_by_id(task_id : int, db: AsyncSession = Depends(get_db)):
    try:
        task = await db_operations.get_task(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        logger.exception(f"An unexpected error occurred while getting the task with task_id:{task_id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/update_task/{task_id}", response_model= TaskResponse)
async def update_task(task_id: int, task_data: TaskUpdate, db: AsyncSession = Depends(get_db)):
    try:
        task = await db_operations.update_task(db, task_id, task_data)
        if not task:
            logger.error("Error while updating task")
            raise HTTPException(status_code=404, detail="Task not found")         
        logger.info(f"Task with task_id:{task_id} updated successfully")
        return task
    except Exception as e:
        logger.exception("An unexpected error occurred while updating a task")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.patch("/mark_completed/{task_id}", response_model= TaskResponse)
async def mark_task_as_completed(task_id: int, task_data: TaskStatusUpdate, db: AsyncSession = Depends(get_db)):
    try:
        task = await db_operations.update_task(db, task_id, task_data)
        if not task:
            logger.error("Error while updating task")
            raise HTTPException(status_code=404, detail="Task not found")         
        logger.info(f"Task with task_id:{task_id} updated successfully")
        return task
    except Exception as e:
        logger.exception("An unexpected error occurred while updating a task")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete("/delete_task/{task_id}", response_model= TaskResponse)
async def delete_task(task_id : int, db: AsyncSession = Depends(get_db)):
    try:
        task = await db_operations.delete_task(db, task_id)
        if not task:
            logger.error("Error while deleting task")
            raise HTTPException(status_code=404, detail="Task not found")           
        logger.info(f"Task with task_id:{task_id} deleted successfully")
        return task
    except Exception as e:
        logger.exception("An unexpected error occurred while creating a task")
        raise HTTPException(status_code=500, detail="Internal Server Error")