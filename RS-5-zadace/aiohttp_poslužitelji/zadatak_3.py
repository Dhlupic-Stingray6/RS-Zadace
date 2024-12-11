from aiohttp import web
import json

korisnici = [
        {'ime': 'Ivo', 'godine': 25},
        {'ime': 'Ana', 'godine': 17},
        {'ime': 'Marko', 'godine': 19},
        {'ime': 'Maja', 'godine': 16},
        {'ime': 'Iva', 'godine': 22}
    ]

def handler_function(request):

    punoljetni = [user for user in korisnici if user['godine'] > 18]

    return web.json_response(punoljetni)

app = web.Application()

app.router.add_get('/korisnici', handler_function)


web.run_app(app, port=8082)

