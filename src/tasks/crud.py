from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.tasks.models import Task
from src.tasks.schemas import TaskCreate

class db_operations:
    async def create_task(db: AsyncSession, task_data: dict):
        new_task = Task(**task_data)
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        return new_task

    async def get_tasks(db: AsyncSession):
        result = await db.execute(select(Task))
        return result.scalars().all()
    
    async def get_max_task_id(db: AsyncSession):
        result = await db.execute(select(func.max(Task.id)))
        max_id = result.scalar()
        return max_id

    async def get_task(db: AsyncSession, task_id: int):
        return await db.get(Task, task_id)


    async def update_task(db: AsyncSession, task_id: int, task_data: dict):
        task = await db.get(Task, task_id)
        if task:
            for key, value in task_data.model_dump().items():
                setattr(task, key, value)
            await db.commit()
        return task


    async def delete_task(db: AsyncSession, task_id: int):
        task = await db.get(Task, task_id)

        if task:
            await db.delete(task)
            await db.commit()
        return task
