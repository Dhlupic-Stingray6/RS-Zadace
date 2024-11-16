#Pojasnite zašto sljedeća petlja nema (previše) smisla:
for i in range(1, 2):
    print(i)

#nema smisla jer se ne ponavlja, već se izvršava samo jednom. početna vrijednost je 1. 
# kako je krajna vrijednost 2, neće napravit povljanje, što onda petlja gubi smisao


#Što će ispisati sljedeća petlja?
for i in range(1, 10, 2):
    print(i)

#ispisuje 1 3 5 7 9

#Što će ispisati sljedeća petlja?
for i in range(10, 1, -1):
    print(i)
#ispisuje 10 9 8 7 6 5 4 3 2