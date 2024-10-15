import asyncio
import time
from functools import wraps

def timed(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

class DataStore:
    def __init__(self):
        self.store = {}
        self.expiry_times = {}

    @timed
    async def set(self, key, value):
        self.store[key] = value
        if key in self.expiry_times:
            del self.expiry_times[key]
        return "OK"

    @timed
    async def get(self, key):
        if key in self.store:
            if key in self.expiry_times and time.time() > self.expiry_times[key]:
                await self.delete(key)
                return None
            return self.store[key]
        return None

    @timed
    async def delete(self, key):
        if key in self.store:
            del self.store[key]
            if key in self.expiry_times:
                del self.expiry_times[key]
            return 1
        return 0

    @timed
    async def expire(self, key, seconds):
        if key in self.store:
            self.expiry_times[key] = time.time() + seconds
            return 1
        return 0

    async def _clean_expired_keys(self):
        while True:
            await asyncio.sleep(1)
            to_delete = [key for key, exp_time in self.expiry_times.items() if time.time() > exp_time]
            for key in to_delete:
                await self.delete(key)
    async def keys(self):
        """Return a list of all keys in the data store."""
        return list(self.store.keys())
