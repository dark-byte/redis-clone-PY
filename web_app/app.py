from fastapi import FastAPI, HTTPException
import asyncio

app = FastAPI()
redis_host = '127.0.0.1'
redis_port = 6379

@app.get("/execute/")
async def execute_command(command: str):
    try:
        reader, writer = await asyncio.open_connection(redis_host, redis_port)
        writer.write((command + '\n').encode())
        await writer.drain()
        data = await reader.readline()
        response = data.decode().strip()
        writer.close()
        await writer.wait_closed()
        return {"command": command, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
