from aiohttp import web


async def handle_sum(request):

    
    data = await request.json()
    
    if not data or 'podaci' not in data:
        return web.json_response({'message:' : 'nema prosljeđenih vrijednosti'}, status=404)
    
    data_nums = data.get('podaci')
    zbroj = sum(data_nums)

    return web.json_response({'zbroj' : zbroj })


app = web.Application()
app.router.add_post('/zbroj', handle_sum)
web.run_app(app, host='localhost', port=8083)