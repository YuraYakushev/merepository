import logging
from aiohttp import web
import asyncio
from peewee import DoesNotExist
from models import db, ApiUser, Location, Device

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init_db():
    db.connect()
    db.create_tables([ApiUser, Location, Device], safe=True)
    db.close()

async def create_device(request):
    data = await request.json()
    try:
        device = Device.create(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location_id=data['location_id'],
            api_user_id=data['api_user_id']
        )
        logger.info(f"Device created with id: {device.id}")
        return web.json_response({'status': 'success', 'device_id': device.id})
    except Exception as e:
        logger.error(f"Error creating device: {str(e)}")
        return web.json_response({'status': 'error', 'message': str(e)}, status=500)

async def get_device(request):
    device_id = request.match_info.get('id')
    try:
        device = Device.get(Device.id == device_id)
        return web.json_response({'status': 'success', 'device': model_to_dict(device)})
    except DoesNotExist:
        logger.warning(f"Device not found: {device_id}")
        return web.json_response({'status': 'error', 'message': 'Device not found'}, status=404)

async def update_device(request):
    device_id = request.match_info.get('id')
    data = await request.json()
    try:
        Device.update(**data).where(Device.id == device_id).execute()
        logger.info(f"Device updated with id: {device_id}")
        return web.json_response({'status': 'success'})
    except DoesNotExist:
        logger.warning(f"Device not found: {device_id}")
        return web.json_response({'status': 'error', 'message': 'Device not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating device: {str(e)}")
        return web.json_response({'status': 'error', 'message': str(e)}, status=500)

async def delete_device(request):
    device_id = request.match_info.get('id')
    try:
        device = Device.get(Device.id == device_id)
        device.delete_instance()
        logger.info(f"Device deleted with id: {device_id}")
        return web.json_response({'status': 'success'})
    except DoesNotExist:
        logger.warning(f"Device not found: {device_id}")
        return web.json_response({'status': 'error', 'message': 'Device not found'}, status=404)

app = web.Application()
app.router.add_post('/devices', create_device)
app.router.add_get('/devices/{id}', get_device)
app.router.add_put('/devices/{id}', update_device)
app.router.add_delete('/devices/{id}', delete_device)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
    web.run_app(app)