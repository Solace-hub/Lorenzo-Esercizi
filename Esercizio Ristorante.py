menù = {"Pesto": "7€",
        "Pizza": "9€",
        "Ragù": "10€"
        }

class Ristorante:
    def __init__(self, nome, tipo_cucina, menù):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menù = menù

    
    def descrivi_ristorante(self):
        print(f"Il ristorante '{self.nome}' serve piatti a base {self.tipo_cucina}.")
    
    
    def stato_apertura(self):
        if self.aperto == True:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante ora è aperto")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante ora è chiuso")
    
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menù[piatto] = prezzo
        print(f"{piatto} è stato aggiunto al menù a {prezzo}€.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menù:
            del self.menù[piatto]
            print(f"{piatto} è stato rimosso dal menù")
    
    def stampa_menu(self):
        print("Questo è il menù del ristorante:")
        for piatto in self.menu:  
            prezzo = self.menu[piatto]
            print(f"{piatto}: {prezzo}€")

