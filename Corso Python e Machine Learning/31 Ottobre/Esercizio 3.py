#Scrivete un programma che prenda i nomi degli alunni di una
#classe e i loro voti, quando l’utente scrive media il programma
#andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
#media dei voti.
#Esempio:
#Nome: Giovanni , Media: 7.5
#Nome: Alfredo , Media: 9
#Nome: Michela, Media 10



alunni = {}

while True:
    nome = input("Inserisci il nome dell'alunno (o scrivi 'media' per il calcolo): ")
    if nome == "media":
        break
    else:
        voto = float(input("Inserisci il voto per " + nome ))
        alunni[nome] = voto

print("La media dei voti")
for nome in alunni:
    voto = alunni[nome]
print("Nome: " + nome + ", Media: " + str(voto))