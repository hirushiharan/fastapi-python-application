"""
Module: main.py
Description: Main entry point for starting the FastAPI application.
"""

import uvicorn
from src.py.api import app
from python_utils import Logger

# Constants for log levels
INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"

logger = Logger()


def main():
    """
    Main function to start the FastAPI application with Uvicorn server.

    Runs the Uvicorn server to serve the FastAPI application.
    The server listens on all network interfaces (0.0.0.0) on port 8000.
    """
    try:
        # Run the Uvicorn server
        uvicorn.run('src.py.api:app', host='0.0.0.0', port=8000)
    except Exception as e:
        logger.log(f"Error running the application: {e}", level=ERROR)
        raise


if __name__ == '__main__':
    main()
