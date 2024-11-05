class Libro:
    def __initi__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizion(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine}"