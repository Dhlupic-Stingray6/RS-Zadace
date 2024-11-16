num = int(input("Unesi broj i izračunat ću faktorijel broja: "))
factorial = 1
brojac = 1

while (brojac <= num):
    
    factorial = factorial * brojac
    brojac += 1
    

print(f'Faktorijel broja {num}: {factorial}')