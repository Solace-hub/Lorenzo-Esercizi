#Lista che contiene il risultato delle aree aggiunto successivamente dal decoratore
risultato_delle_aree = []

#Funzioni per il calcolo delle aree
def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato * lato

def area_rettangolo(base, altezza):
    return base * altezza

#Funzione decoratore per aggiungere il risultato alla lista
def salva_risultato(f):
    def wrapper (*args, **kwargs):
        risultato = f(*args, **kwargs)
        risultato_delle_aree.append(risultato)
        return risultato
    return wrapper

#Funzione per il calcolo delle aree
def calcola_aree():
    while True:
        print("1- Triangolo")
        print("2- Quadrato")
        print("3- Rettangolo")
        print("4- Esci")
        selezione = input("Inserisci il numero corrispondente all'opzione")
        if selezione == "1":
            base = int(input("Inserisci la base"))
            altezza = int(input("Inserisci l'altezza"))
            print("Questa è l'area del triangolo", area_triangolo)
        elif selezione == "2":
            lato = int(input("Inserisci il primo lato"))
            lato = int(input("Inserisci il secondo lato"))
            print("Questa è l'area del quadrato", area_quadrato)
        elif selezione == "3":
            base = int(input("Inserisci la base"))
            altezza = int(input("Inserisci l'altezza"))
            print("Questa è l'area del rettangolo", area_rettangolo)
            break
        

