from aiohttp import web


async def handle_multiply(request):

    
    data = await request.json()

    if not data or 'podaci' not in data:
        return web.json_response({'message:' : 'nema prosljeđenih vrijednosti'}, status=404)
    
    data_nums = data.get('podaci')
    umnozak = 1
    for num in data_nums:
        umnozak *= num

    return web.json_response({'umnozak' : umnozak })


app = web.Application()
app.router.add_post('/umnozak', handle_multiply)
web.run_app(app, host='localhost', port=8084)