from aiohttp import web
import json


def handler_function(request):

    proizvodi = [
        {'naziv': 'tipkovnica', 'cijena' : 100, 'količina' : 50},
        {'naziv': 'miš', 'cijena' : 50, 'količina' : 70},
        {'naziv': 'monitor', 'cijena' : 500, 'količina' : 20},
    ]

    return web.json_response(proizvodi)

app = web.Application()

app.router.add_get('/proizvodi', handler_function)


web.run_app(app, port=8081)



#vraća ERR_CONNECTION_REFUSED na http://localhost:8080/proizvodi