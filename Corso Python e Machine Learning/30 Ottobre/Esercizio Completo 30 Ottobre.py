#Chiediamo all'utente di inserire un numero intero positivo
n = int(input("Inserisci un numero intero positivo"))
while n <= 0:
    #Nel caso in cui quest'ultimo non sia un intero positivo, viene richiesto nuovamente il numero
    print("Il numero deve essere positivo")
    n = int(input("Devi inserire un numero positivo"))
    
#Utilizziamo il ciclo for per ricavare la somma pari dei numeri da 1 a n
somma_pari = 0
#Start con 1, con n+1 prendiamo sempre i numeri pari
for i in range(1, n + 1): 
    if i % 2 == 0:
        #Incrementiamo di 1
        somma_pari += i
print("La somma dei numeri pari sono:", n)

#Stessa metolodogia per i numeri dispari
for i in range(1, n + 1):
    #In questo caso deve essere diverso dal pari
    if i % 2 != 0:
        print("Tutti i numeri dispari sono:", i)
