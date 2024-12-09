from aiohttp import web
import json

proizvodi = [
        {'naziv': 'tipkovnica', 'cijena' : 100, 'količina' : 50},
        {'naziv': 'miš', 'cijena' : 50, 'količina' : 70},
        {'naziv': 'monitor', 'cijena' : 500, 'količina' : 20},
    ]

async def get_users(request):

    

    #proizvodi_lista = [(i['naziv'], i['cijena'], i['količina']) for i in proizvodi] - lista vrijednosti
    print(proizvodi)
    return web.json_response(proizvodi)

async def add_users(request):
    proizvod = await request.json()

    proizvodi.append(proizvod)
    print(proizvodi)
    return web.json_response(proizvod)


app = web.Application()

app.router.add_routes([
    web.get('/proizvodi', get_users),
    web.post('/proizvodi', add_users)
])


web.run_app(app, port=8081)

