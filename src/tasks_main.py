# import os
# from fastapi import FastAPI

# from src.tasks import routes
# from src.core.database import init_db

# app = FastAPI(title = "Task managment")

# app.include_router(routes.router)

# @app.lifespan("startup")
# async def on_startup():
#     await init_db()
#     print("Staring the app")

# @app.lifespan("shutdown")
# async def shutdown_event():
#     print("Shutting down gracefully...")

# import os
# from fastapi import FastAPI
# from src.tasks import routes
# from src.core.database import init_db


# # Define the lifespan context manager
# async def app_lifespan():
#     # Actions during startup
#     print("Starting the app")
#     await init_db()
#     yield  # Indicates that the application is running

#     # Actions during shutdown
#     print("Shutting down gracefully...")


# # Create FastAPI app with the lifespan
# app = FastAPI(title="Task Management", lifespan=app_lifespan)

# # Include routes
# app.include_router(routes.router)

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

