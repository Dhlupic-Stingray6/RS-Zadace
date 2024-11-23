



def provjera_lozinke(lozinka):
    lista_grešaka = []
    #listu grešaka popunjavamo sa porukama ako uvjet zadovolji

    if (len(lozinka) < 8 or len(lozinka) > 15 ) :
        lista_grešaka.append("Lozinka mora sadržavati između 8 i 15 znakova!")
        
    if(lozinka.islower() or lozinka.isdigit()):
        lista_grešaka.append("Lozinka mora imati barem jedno veliko slovo i broj!")

    if any (lozinka.lower() == 'lozinka' or lozinka.lower() =='password'): 
        lista_grešaka.append('lozinka ne smije sadržavati riječi \'pasword\' ili \'lozinka\'!')
        #ne provjerava unos "paSSWOrD123"
    if not lista_grešaka:
        lista_grešaka.append("lozinka je jaka")
    
    return lista_grešaka

def ispis_grešaka():
    for greška in provjera_lozinke(lozinka):
        print(greška) 

lozinka = input ('Unesi lozinku: ')
ispis_grešaka();
print(len(lozinka))
