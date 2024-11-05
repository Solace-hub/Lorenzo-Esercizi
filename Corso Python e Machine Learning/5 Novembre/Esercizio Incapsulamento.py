class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.set_titolare(titolare)  
        self.__saldo = saldo_iniziale

    
    def get_titolare(self):
        return self.__titolare

    
    def set_titolare(self, titolare):
        if titolare != "" and titolare != None: 
            self.__titolare = titolare
        else:
            print("Il nome del titolare deve essere specificato")

    
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Depositati {importo}. Il saldo aggiornato è {self.__saldo}")
        else:
            print("Non è stato possibile continuare perché l'importo da depositare deve essere positivo.")

    
    def preleva(self, importo):
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f"Prelevati {importo}. Il saldo aggiornato è {self.__saldo}")
            else:
                print("Fondi insufficienti.")
        else:
            print("Non è stato possibile continuare perché l'importo da depositare deve essere positivo.")

    
    def visualizza_saldo(self):
        print(f"Il saldo aggiornato ad ora è di {self.__saldo}")
        return self.__saldo

#Esempio
conto = ContoBancario("Mario Rossi", 1000)
print("Titolare:", conto.get_titolare())
conto.visualizza_saldo()
conto.deposita(500)
conto.preleva(300)
conto.deposita(-50)
conto.preleva(2000)
conto.set_titolare("Luigi Verdi")
print("Nuovo titolare:", conto.get_titolare())
