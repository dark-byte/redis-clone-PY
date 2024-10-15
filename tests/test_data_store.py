import pytest
import pytest_asyncio
from redis_server.data_store import DataStore
import asyncio

@pytest_asyncio.fixture
async def data_store():
    return DataStore()

@pytest.mark.asyncio
async def test_set_get(data_store):
    await data_store.set('key1', 'value1')
    assert await data_store.get('key1') == 'value1'

@pytest.mark.asyncio
async def test_delete(data_store):
    await data_store.set('key2', 'value2')
    await data_store.delete('key2')
    assert await data_store.get('key2') is None

@pytest.mark.asyncio
async def test_expire(data_store):
    await data_store.set('key3', 'value3')
    await data_store.expire('key3', 1)
    await asyncio.sleep(2)
    assert await data_store.get('key3') is None

# Concurrency Test
@pytest.mark.asyncio
async def test_concurrent_set_operations(data_store):
    await asyncio.gather(
        data_store.set('key_concurrent', 'value1'),
        data_store.set('key_concurrent', 'value2'),
        data_store.set('key_concurrent', 'value3')
    )
    value = await data_store.get('key_concurrent')
    assert value in ['value1', 'value2', 'value3']

# Edge Case Test: Empty key and large value
@pytest.mark.asyncio
async def test_edge_cases(data_store):
    # Empty key
    await data_store.set('', 'empty_key_value')
    assert await data_store.get('') == 'empty_key_value'

    # Large value
    large_value = 'a' * 10000
    await data_store.set('key_large', large_value)
    assert await data_store.get('key_large') == large_value

# Error Handling Test: Incorrect argument count for SET
@pytest.mark.asyncio
async def test_error_handling_incorrect_arguments():
    store = DataStore()
    with pytest.raises(TypeError):
        await store.set('key_only')  # Missing value argument

# Unsupported command example (assuming you handle such errors at server level)
@pytest.mark.asyncio
async def test_unsupported_command():
    # Simulate unsupported command handling
    store = DataStore()
    # Assuming process_command method exists for error handling, modify according to actual implementation
    pass  # Replace with server-side processing logic if needed
