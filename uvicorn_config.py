import os

HOST = os.getenv("HOST", "127.0.0.1")  # The host to bind to
PORT = int(os.getenv("PORT", 9000))  # The port to run the app
WORKERS = int(os.getenv("WORKERS", 4))  # Number of worker processes
RELOAD = os.getenv("RELOAD", "true").lower() == "true"  # Enable/disable auto-reload
LOG_LEVEL = os.getenv("LOG_LEVEL", "info").lower()  # Log level for server output
ACCESS_LOG = os.getenv("ACCESS_LOG", "true").lower() == "true"  # Enable/disable access logs

# Uvicorn configuration
config = {
    "host": HOST,
    "port": PORT,
    "workers": WORKERS,
    "reload": RELOAD,
    "log_level": LOG_LEVEL,
    "access_log": ACCESS_LOG,
}
