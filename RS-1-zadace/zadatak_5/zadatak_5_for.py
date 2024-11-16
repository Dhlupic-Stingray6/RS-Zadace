num = int(input("Unesi broj i izračunat ću faktorijel broja: "))
factorial = 1

for x in range(1, num+1):
    factorial = factorial * x

print(f'Faktorijel broja {num}: {factorial}')