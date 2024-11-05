#Traccia 1
numero = (int(input("Inserisci un numero")))
if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")

#Traccia 2
while True:
    n = int(input("Inserisci un numero positivo"))
    if n < 0:
        print("Invalido, inserisci un numero positivo")

    while n >= 0:
        n -=1 
        print(n)
        
    ripeti = input("Vuoi ripetere? (sì/no): ")
    if ripeti == "no":
        print("Fine.")
        break
    
#Traccia 3
    numeri = int(input("Inserisci una lista di numeri"))
    for numero in numeri: 
        quadrato_del_numero = numero ** 2
        print("Il quadrato del", numero, "è", quadrato_del_numero)

#Traccia 4
    input_numeri = int(input("Inserisci una lista di numeri"))
    if len(input_numeri) == 0:
        print("La lista è vuota")
    else:
        valore_massimo = numeri[0]
        for numero in input_numeri:
            if numero > valore_massimo:
                valore_massimo = numero

        conto = 0
        i = 0
        while i < len(numeri):
            conto += 1
            i += 1
            print("Il numero massimo è", valore_massimo)
            print("Il numero di elementi nella lista è", conto)
