a = int(input("Uneste godinu: "))


if all([a%4==0, a%100!=0]):
    print("Godina ", a, " je prijestupna.")
elif a%400==0:
    print("Godina ", a, " je prijestupna.")
else: 
    print("Godina ", a, " nije prijestupna.")