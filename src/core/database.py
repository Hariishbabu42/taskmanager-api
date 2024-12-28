from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.core.config import config
import os

engine = create_async_engine(config.DATABASE_URL)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session() as session:
        yield session

async def init_db():
    import src.tasks.models  
    async with engine.begin() as conn:
        await conn.run_sync(src.tasks.models.Base.metadata.create_all)
