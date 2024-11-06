class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__garanzia = garanzia

    def get_garanzia(self):
        return self.__garanzia

    def set_garanzia(self, garanzia):
        self.__garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__materiale = materiale

    def get_materiale(self):
        return self.__materiale
    
    def set_materiale(self, materiale):
        self.__materiale = materiale

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Il prodotto '{prodotto.nome}' è stato aggiunto con successo.")

    def vendi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            self._calcola_totale_profitto(profitto)
            print(f"Il prodotto '{prodotto.nome}' è stato venduto con successo e il profitto è: {profitto}")
        else:
            print("Quantità insufficiente")

    def resi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
            print(f"{quantita} prodotto '{prodotto.nome}' ricevute come reso.")

    def _calcola_totale_profitto(self, profitto):
        if hasattr(self, '_totale_profitto'):
            self._totale_profitto += profitto
        else:
            self._totale_profitto = profitto

    def get_totale_profitto(self):
        return getattr(self, '_totale_profitto', 0)




def descrizione_prodotto(prodotto):
    descrizione_prodotto = (f"Nome: {prodotto.nome}, Prezzo di vendita: {prodotto.prezzo_vendita}€, Profitto: {prodotto.calcola_profitto()}€")
    if isinstance(prodotto, Elettronica):
        return descrizione_prodotto + f", Garanzia di tot {prodotto.get_garanzia()} anni"
    elif isinstance(prodotto, Abbigliamento):
        return descrizione_prodotto + f", Materiale di questa qualità: {prodotto.get_materiale()}"
    
    return descrizione_prodotto

                
#Esempio
telefono = Elettronica("Smartphone", 150, 350, 1)
maglietta = Abbigliamento("T-Shirt", 10, 35, "Cotone")

print(descrizione_prodotto(telefono))   
print(descrizione_prodotto(maglietta)) 


    

    