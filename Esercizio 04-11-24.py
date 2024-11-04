class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine."
    

class Biblioteca():
    lista_libri = []
    def __init__(self):
            self.libri = []

    def libro_aggiunto(self, titolo, autore, pagine):
            libro = Libro(titolo, autore, pagine)
            self.libri.append(libro)
    
    def richiesta_aggiunta_libro(self):
        while True:
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            pagine = int(input("Inserisci il numero di pagine totali del libro: "))
            self.libro_aggiunto(titolo, autore, pagine)
            print("Libro aggiunto")
            



                