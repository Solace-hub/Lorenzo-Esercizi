import random

def genera_numeri_casuali():
    numeri = []
    for i in range(5): 
        numero = random.randint(1, 50)
        numeri.append(numero)
    
    with open("numeri.txt", "w") as file:
        for numero in numeri:
            file.write(f"{numero}\n")  
    
    print("Numeri casuali generati e salvati nel file numeri.txt.")

def leggi_numeri_da_file():
    numeri = []
    with open("numeri.txt", "r") as file:
        for line in file:
            numeri.append(int(line))  
    return numeri

def gioco_indovina_numeri():
    numeri = leggi_numeri_da_file()
    print("Numeri da indovinare:")

    indovinati = []
    while len(indovinati) < 2:
        tentativo = input("Indovina un numero: ")
        
        if not tentativo.isdigit():
            print("Inserisci un numero valido: ")
            continue

        numero = int(tentativo)
        
        if numero in numeri and numero not in indovinati:
            indovinati.append(numero)
            print(f"Hai indovinato {numero}. Numeri indovinati finora: {indovinati}")
        else:
            print(f"Il numero {numero} non è corretto o l'hai già indovinato.")

    print(f"Hai vinto! Bravo {indovinati}")
    print(f"I numeri corretti erano: {numeri}")

genera_numeri_casuali()
gioco_indovina_numeri()
