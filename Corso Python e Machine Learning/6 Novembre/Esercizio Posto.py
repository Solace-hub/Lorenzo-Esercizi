class Posto:
    def __init__(self, numero, fila):
        self.numero = numero
        self.fila = fila
        self._occupato = False

    def __get_numero__(self):
        return self._numero
    
    def __get_fila__(self):
        return self._fila
    
    def __occupato__(self):
        return self._occupato

    def prenota(self):
        if not self._occupato():
            self._occupato = True
            print("Il posto è stato prenotato")
        else:
            print("Il posto è occupato")
    
    def libera(self):
        if self._occupato():
            self._occupato = False
            print("Il posto è stato liberato")
        else:
            print("Il posto è già libero")

    
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra
    
    def prenota(self):
        super().prenota()
        print("Servizi extra inclusi:", self.servizi_extra)


class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_aggiuntivo):
        super().__init__(numero, fila)
        self.costo_aggiuntivo = costo_aggiuntivo


class Teatro:
    def __init__(self):
        self._posti = {}

    def aggiungi_posto(self, posto):
        self._posti[(posto.fila, posto.numero)] = posto

    def prenota_posto(self, fila, numero):
        posto = self._posti.get((fila, numero))
        if posto:
            if posto._occupato():
                print("Posto già occupato.")
            else:
                posto.prenota()
        else:
            print("Posto non trovato.")

    def stampa_posti_occupati(self):
        for (fila, numero), posto in self._posti.items():
            if posto._occupato():
                print(f"Posto {fila}{numero} occupato.")






'''teatro = Teatro()
posto1 = Posto("C", 11)
teatro.aggiungi_posto(posto1)
teatro.prenota_posto("C", 11)
teatro.stampa_posti_occupati()'''
