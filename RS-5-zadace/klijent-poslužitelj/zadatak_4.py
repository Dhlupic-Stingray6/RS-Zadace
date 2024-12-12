from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp


proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]
async def get_items(request):
  return web.json_response(proizvodi, status=200)

async def get_item (request):
    
    user_id = request.match_info['id']

    if user_id is None:
        return web.json_response(proizvodi, status=200)

    for proizvod in proizvodi:
        if proizvod['id'] == int(user_id):
            return web.json_response(proizvod, status=200)


    return web.json_response({'error': f'Proizvod s trazenim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_items)
app.router.add_get('/proizvodi/{id}', get_item)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")


async def main():
    await start_server() # Prvo pokreni poslužitelj
    async with aiohttp.ClientSession() as session: # Zatim otvori klijentsku sesiju
        print("Klijentska sesija otvorena")
        rez1 = await session.get('http://localhost:8080/proizvodi')
        rez1_dict = await rez1.json()
        print(rez1_dict)

        rez2 = await session.get('http://localhost:8080/proizvodi/5')
        rez2_dict = await rez2.json()
        print(rez2_dict)
        
        rez0 = await session.get('http://localhost:8080/proizvodi/50')
        rez0_dict = await rez0.json()
        print(rez0_dict)

asyncio.run(main()) # Pokreni main korutinu