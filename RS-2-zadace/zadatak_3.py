#List comprehension
#[expression for element in iterable if condition]
#[expression1 if condition else expression 2 for element in iterable]

#dictionary comprehension
#{key_expression: value_expression for item in iterable if condition}


#1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:

parni_kvadrati = [x**2 for x in range(20,51) if x%2==0]


print(parni_kvadrati)

#2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
#   sadrže slovo a :

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if 'a']

print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]


#3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti
#   kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:

kubovi = [ {x:x**3} if x%2 == 1 else {x: x} for x in range(1,11)  ]


print(kubovi)


#4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s
#  korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:


korijeni = {x: round(x**0.5,2) for x in range (50,501,50)}

print(korijeni)

#5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti
#   su zbrojeni bodovi, iz liste studenti :

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]


zbrojeni_bodovi = [ {student['prezime']: sum(student['bodovi'])}  for student in studenti]

print(zbrojeni_bodovi)