class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita / self.costo_produzione
    




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

        def aggiungi_prodotto(self, prodotto, quantità):
            if prodotto in self.inventario:
                self.inventario[prodotto] += quantità
            print(f"Il {prodotto} è stato aggiunto con successo")

        def vendi_prodotto(self, prodotto, quantità):
            if prodotto in self.inventario and self.inventario[prodotto] >= quantità:
                self.inventario[prodotto] -= quantità
                profitto = prodotto * quantità
            print(f"Il {prodotto} è stato venduto con successo e il profitto ammonta a: {profitto} ")

        def resi_prodotto(self, prodotto, quantità):
            if prodotto in self.inventario:
                self.inventario[prodotto] += quantità
                print(f"{prodotto} e {quantità} ricevuti come reso in deposito")
                



'''prodotto1 = Prodotto("Smartphone", 100, 350)
fabbrica = Fabbrica()
fabbrica.aggiungi_prodotto(prodotto1, 10)
fabbrica.vendi_prodotto(prodotto1, 3)
fabbrica.resi_prodotto(prodotto1, 1)
'''

    

    