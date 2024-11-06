class Prodotto:
    def ____init____(self, nome, costo__produzione, prezzo__vendita):
        self.nome = nome
        self.costo__produzione = costo__produzione
        self.prezzo__vendita = prezzo__vendita

    def calcola__profitto(self):
        return self.prezzo__vendita - self.costo__produzione

class Elettronica(Prodotto):
    def ____init____(self, nome, costo__produzione, prezzo__vendita, garanzia):
        super().____init____(nome, costo__produzione, prezzo__vendita)
        self.____garanzia = garanzia

    def get__garanzia(self):
        return self.____garanzia

    def set__garanzia(self, garanzia):
        self.____garanzia = garanzia

class Abbigliamento(Prodotto):
    def ____init____(self, nome, costo__produzione, prezzo__vendita, materiale):
        super().____init____(nome, costo__produzione, prezzo__vendita)
        self.____materiale = materiale

    def get__materiale(self):
        return self.____materiale
    
    def set__materiale(self, materiale):
        self.____materiale = materiale

class Fabbrica:
    def ____init____(self):
        self.inventario = {}

    def aggiungi__prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Il prodotto '{prodotto.nome}' è stato aggiunto con successo.")

    def vendi__prodotto(self, prodotto, quantita):
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola__profitto() * quantita
            self.__calcola__totale__profitto(profitto)
            print(f"Il prodotto '{prodotto.nome}' è stato venduto con successo e il profitto è: {profitto}")
        else:
            print("Quantità insufficiente")

    def resi__prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
            print(f"{quantita} prodotto '{prodotto.nome}' ricevute come reso.")

    def __calcola__totale__profitto(self, profitto):
        if hasattr(self, '__totale__profitto'):
            self.__totale__profitto += profitto
        else:
            self.__totale__profitto = profitto

    def get__totale__profitto(self):
        return getattr(self, '__totale__profitto', 0)




def descrizione__prodotto(prodotto):
    descrizione__prodotto = (f"Nome: {prodotto.nome}, Prezzo di vendita: {prodotto.prezzo__vendita}€, Profitto: {prodotto.calcola__profitto()}€")
    if isinstance(prodotto, Elettronica):
        return descrizione__prodotto + f", Garanzia di tot {prodotto.get__garanzia()} anni"
    elif isinstance(prodotto, Abbigliamento):
        return descrizione__prodotto + f", Materiale di questa qualità: {prodotto.get__materiale()}"
    
    return descrizione__prodotto

                
#Esempio
telefono = Elettronica("Smartphone", 150, 350, 1)
maglietta = Abbigliamento("T-Shirt", 10, 35, "Cotone")

print(descrizione__prodotto(telefono))   
print(descrizione__prodotto(maglietta)) 


    

    