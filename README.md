# Mini Redis Clone

A simplified Redis clone in Python that supports basic Redis commands and includes persistence, concurrency, and a web interface.

## Features
- **Commands**: Supports Redis-like commands: `SET`, `GET`, `DEL`, and `EXPIRE`.
- **Persistence**: Saves and loads data to/from a file, allowing data to persist between restarts.
- **Concurrency**: Manages multiple clients using `asyncio`.
- **Web Interface**: Interact with the Redis clone through a FastAPI web application.

## Prerequisites
- Python 3.7 or higher

## Setup Instructions

### 1. Clone or Download the Project
Clone this repository or download the ZIP file and extract it.

### 2. Navigate to the Project Directory
Open a terminal and navigate to the `redis-clone-PY` directory.

### 3. Install Dependencies
Use `pip` to install the required Python packages. Ensure you have Python 3.7 or above.
```bash
pip install -r requirements.txt