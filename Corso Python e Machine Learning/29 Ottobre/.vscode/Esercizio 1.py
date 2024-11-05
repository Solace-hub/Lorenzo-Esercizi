while True: 
#Chiediamo all'utente se inserire un numero o una stringa
    scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa)")
    if scelta == "numero":
        numero = int(input("Inserisci numero: "))

        #Calcola il resto della divisione di due numeri, se 0 pari, se 1 dispari
        if numero % 2 == 0: 
            print(int(numero) + "è un numero pari")
        else:
            print(int(numero) + "è un numero dispari")
    elif scelta == "stringa":
        stringa = input("Inserisci una stringa")
        print("Hai inserito una stringa")

    #Qui chiediamo all'utente se vuole ripetere il procedimento
    ripetizione = input("Desideri ripetere? (sì/no)")
    if ripetizione == "no":
        print("Fine.")