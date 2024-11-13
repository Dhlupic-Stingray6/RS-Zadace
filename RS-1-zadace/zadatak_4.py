'''
Vježba 4: Analiziraj sljedeće while petlje
Pokušajte pogoditi što će se ispisati tijekom izvođenja sljedeće petlje:

broj = 0
while broj < 5:
    broj +=2  
    print(broj)     ispis je 2,4,6. 6 ispisuje iz razloga što je broj = 4 kod zadnjeg ponavljanja, a zadovoljava while uvijet 

#Objasnite zašto se prikazana petlja beskonačna:

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1     beskonačna petlja iz razloga što je broj uvijek isti (0) kod izlaska iz petlje, a ispisuje 1


#Navedite što "ne valja" u sljedećoj petlji:
broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2

#isto beskonačna petlja, prvo će brojač ispisati brojeve 9,8,7,6,5,4 i onda će vrtiti beskonačnu petlju sa ispisom 5 i 4
# varijabla broj izvan petlje, ide prvo 10 pa onda 9,8,7,6,5 . kod 5 se prvo broj smanjuje na 4 koji ispunjava if , i unutar if bloka mijenja se varijabla na 6 pa 5 i 4 i tako u krug 

'''