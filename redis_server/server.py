import asyncio
from persistence import Persistence
from data_store import DataStore

class RedisServer:
    def __init__(self, host='127.0.0.1', port=6379, save_interval=10):
        self.host = host
        self.port = port
        self.data_store = DataStore()
        self.persistence = Persistence(self.data_store, save_interval=save_interval)

    async def handle_client(self, reader, writer):
        address = writer.get_extra_info('peername')
        print(f"New connection from {address}")

        while True:
            data = await reader.readline()
            if not data:
                print(f"Connection closed by {address}")
                break

            message = data.decode().strip()
            print(f"Received command: {message}")

            response = await self.process_command(message)

            writer.write((response + '\n').encode())
            await writer.drain()

        writer.close()
        await writer.wait_closed()

    async def process_command(self, message):
        try:
            parts = message.split()
            command = parts[0].upper()

            if command == 'SET' and len(parts) == 3:
                _, key, value = parts
                result = await self.data_store.set(key, value)
                return result
            elif command == 'GET' and len(parts) == 2:
                _, key = parts
                result = await self.data_store.get(key)
                return result if result is not None else "(nil)"
            elif command == 'DEL' and len(parts) == 2:
                _, key = parts
                result = await self.data_store.delete(key)
                return "(integer) " + str(result)
            elif command == 'EXPIRE' and len(parts) == 3:
                _, key, seconds = parts
                result = await self.data_store.expire(key, int(seconds))
                return "(integer) " + str(result)
            elif command == 'KEYS':
                keys = await self.data_store.keys()
                return str(keys)
            else:
                return "ERROR: Unsupported command or wrong number of arguments"
        except Exception as e:
            return f"ERROR: {str(e)}"

    async def start(self):
        await self.persistence.load_from_file()
        asyncio.create_task(self.persistence.auto_save())

        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            print(f"Serving on {self.host}:{self.port}")
            await server.serve_forever()

if __name__ == "__main__":
    redis_server = RedisServer()
    asyncio.run(redis_server.start())
