import random
#Inizio della funzione
def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    print("Ecco un numero casuale tra 1 e 100, indovina")
    print("Digita 'esci' per uscire dal gioco")
#Ciclo in while per la decisione dell'utente
    while True:
        scelta = input("Inserisci la tua prima scelta")
        if scelta == "esci":
            print("Fine del gioco")
    
#Se l'utente non inserisce tutti caratteri numeri, riporta la dicitura che non è valido
        if not scelta.isdigit():
            print("Inserisci un numero valido")
        continue

scelta = int(scelta)
if scelta < indovina_il_numero:
        print("Il numero indovinato è più alto")
elif scelta > indovina_il_numero:
        print("Il numero indovinato è più basso ")
else:
        print("Bravo, hai indovinato il numero")