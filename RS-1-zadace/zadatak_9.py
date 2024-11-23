lista = [1,2,3,4,5,1,2,3,4,5]

skup = set()

def ukloni_duplikate(lista):
    for element in lista:
        skup.add(element)

    lista = []

    for element in skup:
        lista.append(element)


    return lista


print(ukloni_duplikate(lista))