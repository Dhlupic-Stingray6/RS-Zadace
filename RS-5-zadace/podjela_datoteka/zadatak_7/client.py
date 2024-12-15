import aiohttp
import asyncio



async def fetch_sum_data(session, data_json):
    response = await session.post('http://localhost:8083/zbroj', json=data_json)
    return await response.json()


async def fetch_multiplied_data(session, data_json):
    response = await session.post('http://localhost:8084/umnozak', json=data_json)
    return await response.json()


async def main():
    print('Pokrećem main korutinu')
    data = [1,2,3,4,5,6,7,8,9,10]
    data_json = {'podaci' : data}

    async with aiohttp.ClientSession() as session:
       #slanje na 1. mikroservis
        microservice_sum_data, microservice_multiply_data = await asyncio.gather(
            fetch_sum_data(
                session,
                data_json
            ), 
            fetch_multiplied_data(
                session,
                data_json
            )
        )



        zbroj = microservice_sum_data.get('zbroj')
        umnozak = microservice_multiply_data.get('umnozak')   


        microservice_ratio_result = await session.post('http://localhost:8085/kolicnik', json= {
            'zbroj' : zbroj, 
            'umnozak': umnozak
        })

        kolicnik = await microservice_ratio_result.json()
        
        print(f'Zbroj: {zbroj}')
        print(f'Umnozak: {umnozak}')
        print(f'Kolicnik: {kolicnik}')



        
asyncio.run(main())
