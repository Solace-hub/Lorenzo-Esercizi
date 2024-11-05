#Scrivete un programma che utilizza una funzione che accetta
#come parametro una stringa passata dall'utente e restituisce
#in risposta se è palindroma o no.

def is_palindroma(frase):
    frase_pulita = " "
    for carattere in frase:
        if carattere.isalnum():
            frase_pulita += carattere.lower()  
    if frase_pulita == frase_pulita[ : : -1]:
        return "La frase è palindroma"
    else:
        return "La frase non è palindroma"
frase_utente = input("Inserisci una frase per verificare se è palindroma: ")
risultato = is_palindroma(frase_utente)
print(risultato)

