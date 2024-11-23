lista = [1,2,3,4,5,6,7,8,9,10]

def filtriraj_parne(lista):
    for element in lista:
        if(element % 2 != 0):
            lista.remove(element)
        
filtriraj_parne(lista);
print(lista)
