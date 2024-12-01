import asyncio


baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autentifikacija(user):
    print('autentifikacija korisnika...', user['korisnicko_ime'])

    await asyncio.sleep(3)

    provjera = any(
        [k['korisnicko_ime'] == user['korisnicko_ime'] and k['email'] == user['email']  for k in baza_korisnika ])

    if provjera:
        print('ok')
       
    else:
        print('not ok')

    return provjera, 

async def autorizacija(user, password):
    print('autorizacija korisnika...', user['korisnicko_ime'] )

    await asyncio.sleep(2)

    provjera = any(
        [lozinka['lozinka'] == password['lozinka'] for lozinka in baza_lozinka ])
    
    if provjera:
        print('password ok')
    else:
        print('password not ok')

async def main():

    print('Upišite podatke za autentifikaciju')
    korisnik_ime = input('Upišite korisničko ime: ')
    korisnik_email = input('Upišite email: ')

    korisnik = {'korisnicko_ime': korisnik_ime, 'email' : korisnik_email}

    #print(korisnik)
    
    await asyncio.gather(
        autentifikacija(korisnik)
       
        
    )



    #print(rezultat)

asyncio.run(main())