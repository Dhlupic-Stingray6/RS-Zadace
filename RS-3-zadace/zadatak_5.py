import asyncio

podaci = [
    {'prezime': 'Mirkovic', 'broj_kartice': '1234567890' , 'CVV': '123'},
    {'prezime': 'Ivkovic', 'broj_kartice': '9876543210', 'CVV': '321'},
    {'prezime': 'Peric', 'broj_kartice': '1122334455', 'CVV': '222'},
]

async def secure_data(osjetljivi):
   
    osjetljivi = [(data['prezime'], hash(data['broj_kartice']), hash(data['CVV'])) for data in osjetljivi]
    
    await asyncio.sleep(3)

   
    print(osjetljivi)
    

async def main():
    print('Enkripcija podataka...')

    zadaci = [asyncio.create_task(secure_data(podaci))]

    await asyncio.gather(*zadaci)

asyncio.run(main())
