#Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
#   listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
#   korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
#   sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
#   se mora izvršavati ~5 sekundi.
import asyncio

async def korisnik():
    print('dohvaćam podatke o korisnicima...')
    await asyncio.sleep(3)
    korisnici = [
        {'ime': 'mirko', 'godiste' : '1989', 'email': 'mirko@gmail.com'},
        {'ime': 'ana', 'godiste' : '2000', 'email': 'ana123@gmail.com'},
        {'ime': 'ivan', 'godiste' : '2006', 'email': 'ivan123@gmail.com'}
        ]
    
    lista_korisnika = [ (user['ime'], user['godiste'], user['email']) for user in korisnici]
    
    
    print('podaci o korisnicima su dohvaćeni')
   
    return lista_korisnika


async def proizvod():
    print('dohvaćam podatke o proizvodima')
    await asyncio.sleep(5)
    proizvodi =[
        {'naziv': 'samsung', 'tip' : 'tv', 'cijena' : 1500},
        {'naziv': 'iphone 15', 'tip' : 'mobitel', 'cijena' : 1000},
        {'naziv': 'tesla', 'tip' : 'automobil', 'cijena' : 45000},
    ]

    lista_proizvoda = [(p['naziv'], p['tip'], p['cijena']) for p in proizvodi]

    
    print('podaci o proizvodima su dohvaćeni')

    return lista_proizvoda

async def main():
   
    korisnici_podaci, proizvodi_podaci = await asyncio.gather(korisnik(), proizvod())
    
    


    print(f'korisinci: {korisnici_podaci}')
    print(f'proizvodi: {proizvodi_podaci}')


asyncio.run(main())