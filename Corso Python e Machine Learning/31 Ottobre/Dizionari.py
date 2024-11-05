#Scrivete un programma che chiede una stringa all'utente e restituisce un dizionario rappresentante
#la "frequenza di comparsa" di ciascun carattere componente la stringa.


stringa = input("Inserisci una stringa")
freq_comparsa_char = {}

for carattere in stringa:
    if carattere in (str(freq_comparsa_char)):
        freq_comparsa_char[carattere] += 1
    else:
        freq_comparsa_char[carattere] = 1
    print(freq_comparsa_char, carattere)