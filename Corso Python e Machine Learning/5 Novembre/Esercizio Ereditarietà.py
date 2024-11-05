class Zoo:
    lista_animali = []
    def aggiungi_animali(self):
        if True:
            cane = Cane()
            
    
    '''def scegli_animale(self):
        print("Scegli l'animale:")
        print("1 - Cane")
        print("2 - Gatto")
        print("3 - Pesce")
        scelta = input("Scegli il numero dell'animale: ")

        nome = input("Inserisci il nome dell'animale: ")
        età = int(input("Inserisci l'età dell'animale: "))'''



class Animale():
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def fai_suono(self):
        pass


class Cane(Animale):
    def __init__(self, nome, età, razza):
        super().__init__(nome, età)
        self.razza = razza
    
    def fai_suono(self):
        print(f"{self.nome} abbaia")
    
    def corsa(self):
        print(f"{self.nome} corre lungo il prato")


class Gatto(Animale):
    def __init__(self, nome, età, colore):
        super().__init__(nome, età)
        self.colore = colore

    def fai_suono(self):
        print(f"{self.nome} miagola")

    def fusa(self):
        print(f"{self.nome} fa le fusa")


class Pesce(Animale):
    def __init__(self, nome, età, ricerca ):
        super().__init__(nome, età)
        self.ricerca = ricerca
    
    def fai_suono(self):
        print(f"{self.nome} stridula")

    def ricerca(self):
        print(f"{self.nome} ricerca i detriti")

    
