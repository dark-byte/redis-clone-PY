import pytest
import pytest_asyncio
from redis_server.data_store import DataStore
from redis_server.persistence import Persistence
import os
import asyncio

@pytest_asyncio.fixture
async def data_store_persistence():
    store = DataStore()
    persistence = Persistence(store, file_path="temp_data_store.json")
    await persistence.save_to_file()  # Start with a clean file
    yield store, persistence
    if os.path.exists("temp_data_store.json"):
        os.remove("temp_data_store.json")

@pytest.mark.asyncio
async def test_persistence_save_load(data_store_persistence):
    store, persistence = data_store_persistence
    await store.set('persistent_key', 'persistent_value')
    await persistence.save_to_file()

    # Clear the in-memory store and reload from file
    await store.delete('persistent_key')
    await persistence.load_from_file()

    assert await store.get('persistent_key') == 'persistent_value'

@pytest.mark.asyncio
async def test_persistence_data_retention_after_reload(data_store_persistence):
    store, persistence = data_store_persistence

    # Store multiple values
    await store.set('key1', 'value1')
    await store.set('key2', 'value2')
    await persistence.save_to_file()

    # Clear the store and reload
    await store.delete('key1')
    await store.delete('key2')
    await persistence.load_from_file()

    assert await store.get('key1') == 'value1'
    assert await store.get('key2') == 'value2'
