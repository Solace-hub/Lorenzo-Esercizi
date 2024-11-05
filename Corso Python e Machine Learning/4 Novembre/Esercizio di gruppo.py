'''def mostra_classifica(self):
        print("Classifica finale:")
        classifica = sorted(self.partecipanti)
        for i, partecipante in enumerate(classifica):
            print(f"{i + 1}. {partecipante.nome}, {partecipante.punteggio} punti")''' #Se con le classi


def punteggio(partecipante):
    #Otteniamo il punteggio del partecipante
    return partecipante['punteggio']

def classifica(partecipanti):
    # Ordina i partecipanti in base al punteggio
    classifica = sorted(partecipanti, key=punteggio, reverse=True)
    print("Classifica finale:")
    for i in range(len(classifica)):
        nome = classifica[i]['nome']
        punteggio = classifica[i]['punteggio']
        print(f"{i + 1}. {nome} {punteggio} punti")

'''partecipanti = [
    {'nome': 'Mario', 'punteggio': 30},
    {'nome': 'Marco', 'punteggio': 20},
    {'nome': 'Ciro', 'punteggio': 40}
]

classifica(partecipanti)'''
