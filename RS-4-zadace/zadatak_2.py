import aiohttp
import asyncio
import time

async def get_cat_fact(session, i):
    
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    #print(f"{i+1} : {fact_dict['fact']}")
    return fact_dict['fact']


async def filter_cat_facts(facts):
    print('šaljemo zahtjev za mačiji fact')
    filtered_list = [fact for fact in facts if 'cat' in fact.lower() or 'cats' in fact.lower() ] 

    return filtered_list

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session, i)) for i in range(20)]

        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)

        filtered_cat_facts = await filter_cat_facts(actual_cat_facts)
        
        
        print('Filtrirane činjenice o mačkama: ')

        [print(f'- {fact} \n') for fact in filtered_cat_facts]

    
    
    
    end = time.time()
    print(f'\nIzvršavanje programa traje {end - start:.2f} sekundi')

asyncio.run(main())