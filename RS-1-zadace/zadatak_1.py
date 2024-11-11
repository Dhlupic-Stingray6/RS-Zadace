a = float(input("Unesite prvi broj: "))
x = input("Unesite operator: ")
b = float(input("Unesite drugi broj: "))


if x == '+' :
    print("Rezultat opercije " , a , "+" ,b, " je " , a+b)
elif x == '-':
    print("Rezultat opercije " , a , "-" ,b, " je " , a-b)
elif x == '*':
    print("Rezultat opercije " , a , "*" ,b, " je " , a*b)
elif any([a ==0, b == 0]):                          
    #https://www.tutorialspoint.com/how-to-check-multiple-variables-against-a-value-in-python
    print("Dijeljenje s nulom nije dozvoljeno!")
elif x == '/':
    print("Rezultat opercije " , a , "/" ,b, " je " , a/b)
else:
    print("Nepodržani operator!") 


