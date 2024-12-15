import aiohttp
import asyncio
import time



async def fetch_service(host: str, port: int):
    url = f'http://{host}:{port}/pozdrav'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

        
    


async def main():
    print('Pokrećem main korutinu')
    
    start_time = time.time()

    results1 = await fetch_service('localhost', 8081)
    results2 = await fetch_service('localhost', 8082)

    end_time = time.time()
    print('Sekvencijalno riješavanje zadatka')
    print(results1)
    print(results2)
    print(f"Vrijeme izvršavanja: {end_time - start_time:.2f} sekundi")

    start_time1 = time.time()

    tasks = [fetch_service('localhost', 8081),fetch_service('localhost',8082)]
    results3 = await asyncio.gather(*tasks)
    
    print('Sekvencijalno riješavanje zadatka: ')
    [print(response) for response in results3]

    end_time1 = time.time()
    
    print(f"Vrijeme izvršavanja: {end_time1 - start_time1:.2f} sekundi")


asyncio.run(main())


'''
ISPIS:

Pokrećem main korutinu
Sekvencijalno riješavanje zadatka
{'message': 'Hello from Microservice1'}
{'message': 'Hello from Microservice2'}
Vrijeme izvršavanja: 7.02 sekundi
Sekvencijalno riješavanje zadatka: 
{'message': 'Hello from Microservice1'}
{'message': 'Hello from Microservice2'}
Vrijeme izvršavanja: 4.01 sekundi



'''