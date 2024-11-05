class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
         return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def mostra_punti(self):
        return f"({self.x}, {self.y})"
    
    
class PianoCartesiano:
    def __init__(self):
        self.punti = []

    def aggiungi_punto(self, punto):
        self.punti.append(punto)

    def stampa_piano(self):
        if len(self.punti) > 1:
            return self.punti 
    
    def muovi_punti(self, dx1, dy1):
        for punto in self.punti:
            punto.muovi_punti(dx1, dy1)
    
    def distanza_origine(self):
        return [punto.distanza_da_origine() for punto in self.punti]
    


    