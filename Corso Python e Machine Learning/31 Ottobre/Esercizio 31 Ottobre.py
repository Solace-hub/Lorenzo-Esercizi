#Scrivete un programma che chiede all'utente una parola e restituisce in output solo le vocali della parola e l'indice 
#della vocale all'interno della parola.

parola = input("Inserisci una parola: ")

for i in range(len(parola)):
    if parola [i] in "aeiou":
        print("Ho trovato questa vocale: " + parola[i] +  " all'indice: " + str(i))