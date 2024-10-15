import json
import os
import asyncio

class Persistence:
    def __init__(self, data_store, file_path='data_store.json', save_interval=10):
        self.data_store = data_store
        self.file_path = file_path
        self.save_interval = save_interval

    async def save_to_file(self):
        try:
            data = {
                'store': self.data_store.store,
                'expiry_times': self.data_store.expiry_times
            }
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    async def load_from_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                self.data_store.store = data.get('store', {})
                self.data_store.expiry_times = data.get('expiry_times', {})
                print("Data loaded successfully.")
            except Exception as e:
                print(f"Error loading data: {e}")

    async def auto_save(self):
        while True:
            await asyncio.sleep(self.save_interval)
            await self.save_to_file()
