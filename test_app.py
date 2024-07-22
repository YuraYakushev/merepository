import pytest
from aiohttp import web
from iot_management.app import app

@pytest.fixture
def cli(loop, aiohttp_client):
    return loop.run_until_complete(aiohttp_client(app))

async def test_create_device(cli):
    data = {
        "name": "Test Device",
        "type": "Sensor",
        "login": "test_login",
        "password": "test_password",
        "location_id": 1,
        "api_user_id": 1
    }
    resp = await cli.post('/devices', json=data)
    assert resp.status == 200
    result = await resp.json()
    assert result['status'] == 'success'

async def test_get_device(cli):
    resp = await cli.get('/devices/1')
    assert resp.status == 200
    result = await resp.json()
    assert result['status'] == 'success'
    assert result['device']['name'] == 'Test Device'