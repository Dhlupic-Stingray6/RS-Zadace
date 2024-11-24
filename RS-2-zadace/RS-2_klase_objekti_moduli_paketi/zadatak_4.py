from datetime import date
import math #za pi

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        return f' Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraža} km'
    
    def starost(self):
        return  date.today().year - self.godina_proizvodnje

automobil = Automobil('Toyota', 'Aygo', 2016, 115000)


print(automobil.ispis())
print(automobil.starost())




#########################################################################



class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return f'{self.a}+{self.b} = {self.a+self.b}'
    
    def subtract(self):
        return f'{self.a}-{self.b} = {self.a-self.b}'
    
    def multiply(self):
        return f'{self.a}*{self.b} = {self.a*self.b}'
    
    def divide(self):
        return f'{self.a}/{self.b} = {self.a/self.b}'
    
    def exponential(self):
        return f'{self.a} sa potencijom {self.b} je {self.a**self.b}'
    
    def root(self):
        return f'korijen {self.a} na {self.b} je {self.a**(1/self.b)}'


a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

izračunaj = Kalkulator(a,b)

print(izračunaj.add())
print(izračunaj.subtract())
print(izračunaj.multiply())
print(izračunaj.divide())
print(izračunaj.exponential())
print(izračunaj.root())




####################################################################################
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene


    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    


studenti_objekti = [student for student in studenti]
#najbolji_student = max(studenti_objekti, lambda student: student.prosjek())



#print(studenti_objekti)
#print(najbolji_student)




#####################################################################################

class Krug:
    def __init__(self, r):
        self.r = r


    def opseg(self):
        return 2*math.pi*self.r
    
    def površina(self):
        return (self.r**2)*math.pi
    

r = int(input("Unesi radijus kruga: "))

izracunaj_krug= Krug(r)

print(izracunaj_krug.opseg())
print(izracunaj_krug.površina())


############################################################################################


class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa


    def work(self):
        return f'Ja {self.ime} radim na poziciji {self.pozicija}.'
    

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        return f'Ja {self.ime} radim na poziciji {self.pozicija} u odjelu {self.department}'
    
    def give_raise(self,radnik, povecanje):
        self.radnik = radnik
        self.povecanje = povecanje
        return f'Plaća radniku {self.radnik.ime} je povećana na {self.radnik.placa+self.povecanje} kuna'
    

radnik = Radnik('Mirko', 'Zidar', 5000)
manager = Manager('Štef', 'Voditelj tima', 8000, 'Projekti')

print(radnik.work())
print(manager.work())
print(manager.give_raise(radnik, 1000))