class MetodoPagamento:
    def effettua_pagamento(self, importo):
        pass

class CartaDiCredito(MetodoPagamento):
    def __init__(self, numero_carta, titolare):
        self.numero_carta = numero_carta
        self.titolare = titolare


    def __verifica_fondi(self, importo):
        return importo < 2500

    
    def effettua_pagamento(self, importo):
        if self.__verifica_fondi(self, importo):
            print(f"Pagamento di {importo} effettuato per conto di {self.__titolare} con numero di carta {self.__numero_carta}.")
        else:
            print("Non abbastanza fondi per effettuare il pagamento")

    
    def numero_carta(self):
        return self.__numero_carta
    
    
    def numero_carta(self, numero):
        if len(numero) == 16 and numero.isdigit():
            self.__numero_carta = numero
        else:
            print("Numero di carta non valido")


class PayPal(MetodoPagamento):
    def __init__(self, username):
        self.username = username 

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo} effettuato da {self.username}") 


class BonificoBancario(MetodoPagamento):
    def __init__(self, iban, banca):
        self.iban = iban
        self.banca = banca
    
    def effettua_pagamento(self, importo, banca):
        if self.__controllo_richiesta(importo):
            print(f"Pagamento di {importo} effettuato tramite Bonifico Bancario sull'IBAN {self.iban} dalla banca {self.banca}")
        else:
            print("Non è stato possibile effettuare il bonifico")


class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def utilizza_metodo(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)
