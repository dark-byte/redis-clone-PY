<h1 align="center" id="title">In-Memory Key-Value Store (Redis)</h1>

<p align="center"><img src="https://socialify.git.ci/dark-byte/redis-clone-PY/image?language=1&amp;owner=1&amp;name=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">A simplified Redis clone in Python that supports basic Redis commands and includes persistence concurrency and a web interface.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Commands: Supports Redis-like commands: SET GET DEL and EXPIRE.
*   Persistence: Saves and loads data to/from a file allowing data to persist between restarts.
*   Concurrency: Manages multiple clients using asyncio.
*   Web Interface: Interact with the Redis clone through a FastAPI web application.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone or Download the Project</p>

```
git clone https://github.com/dark-byte/redis-clone-PY
```

<p>2. Navigate to the Project Directory</p>

```
cd redis-clone-PY
```

<p>3. Install Dependencies</p>

```
pip install -r requirements.txt
```

<p>4. Run the Server</p>

```
python -m redis_server.server
```

<p>5. Start the FastAPI Web App</p>

```
uvicorn web_app.app:app --reload
```

<p>6. Access the Web Interface</p>

```
http://127.0.0.1:8000
```

<p>7. Open a browser and go to http://127.0.0.1:8000/execute/?command=SET+mykey+Hello. Replace SET+mykey+Hello with any valid command</p>

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Asyncio
*   FastAPI
*   uvivorn
*   Pytest
