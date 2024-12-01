import asyncio
import random

async def provjeri_parnost(broj):
    
    await asyncio.sleep(2)

    

 
    if broj %2 == 0:
        print(broj , ' je paran broj')

    else:
        print(broj ,' je neparan broj')


async def main():
    print('radim super zahtjevnu operaciju...')
   
 
    lista = [random.randint(1,100) for broj in range(1,11) ]
    print('lista' , lista)

    zadaci = [asyncio.create_task(provjeri_parnost(lista[i])) for i in range(10)]

    await asyncio.gather(*zadaci)

asyncio.run(main())