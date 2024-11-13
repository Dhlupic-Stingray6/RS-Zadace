import random   #https://docs.python.org/3/library/random.html#random.randint
broj_je_pogoden = False

rjesenje = random.randint(1,99)  #korištena funkcija za generiranje slučajnog broja u intervalu (a,b+1)
#print(rjesenje)
brojac = 1
uneseni_broj = int(input('Ovo je igra pogađanja brojeva od 1 do 100. Pogodi broj! '))

while (broj_je_pogoden != True):
    if(any([uneseni_broj<1 , uneseni_broj>100])):
        print('potrebno je unijeti broj koji je od 1 do 100! ')
        uneseni_broj = int(input('pokusaj ponovno: '))
    elif(uneseni_broj>rjesenje):
        print('broj je veci od unesenog')
        uneseni_broj = int(input('pokusaj ponovno: '))
        brojac = brojac + 1
    elif(uneseni_broj<rjesenje):
        print('broj je manji od unesenog')
        uneseni_broj = int(input('pokusaj ponovno: '))
        
        brojac = brojac + 1
    else:
        broj_je_pogoden = True
        
print('Bravo, pogodio si u', brojac , 'pokušaja!')




