# Decoratore per controllare se la compressione è necessaria
def verifica_compressione(f):
    def wrapper(stringa):
        stringa_compressa = f(stringa)
        if len(stringa_compressa) >= len(stringa):
            return stringa
        return stringa_compressa
    return wrapper

# Funzione per comprimere la stringa
@verifica_compressione
def compressione_stringa(stringa):
    risultato = " "
    conteggio = 1

    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:
            conteggio += 1
        else:
            risultato += stringa[i - 1] + str(conteggio)
            conteggio = 1
    
    risultato += stringa[-1] + str(conteggio)
    return risultato