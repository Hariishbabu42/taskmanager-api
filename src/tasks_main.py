import os
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.tasks import routes
from src.core.database import init_db

app = FastAPI(title="Task Management")

app.include_router(routes.router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Starting the app")
    yield 
    print("Shutting down gracefully...")

app.router.lifespan_context = lifespan

