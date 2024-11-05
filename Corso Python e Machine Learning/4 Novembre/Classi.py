class Automobile:
    numero_di_route = 4
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        def stampa_info(self):
            print("L'automobile è una", self.marca, self.modello, self.numero_di_ruote)

            #Negli oggetti self è un placeholder che serve a sostituire il nome reale dell'oggetto
            #Init è il costruttore, serve a costruire l'oggetto della classe automobile, dà valore alla variabile
            #auto1 = Automobile("Fiat", "500") #In questo caso, auto1 è il nostro self


           