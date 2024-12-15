import aiohttp
from aiohttp import web
import asyncio


app = web.Application()

async def handle_ratio(request):

    data = await request.json()
    zbroj = data.get('zbroj')
    umnozak = data.get('umnozak')

    if umnozak == 0:
        return web.json_response({'message': 'nemoguće je dijeliti s nulom'}, status=404)
    else:
        kolicnik = umnozak/zbroj

    return web.json_response(round(kolicnik, 4))


app.router.add_post('/kolicnik', handle_ratio)
web.run_app(app, host='localhost', port=8085)