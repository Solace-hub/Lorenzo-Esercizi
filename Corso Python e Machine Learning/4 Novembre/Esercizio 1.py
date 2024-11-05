class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return self.x, self.y
    
    
