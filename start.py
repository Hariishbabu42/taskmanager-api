import uvicorn
import uvicorn_config

if __name__ == "__main__":
    uvicorn.run(
        "src.tasks_main:app",
        host=uvicorn_config.config["host"],
        port=uvicorn_config.config["port"],
        workers=uvicorn_config.config["workers"],
        reload=uvicorn_config.config["reload"],
    )
