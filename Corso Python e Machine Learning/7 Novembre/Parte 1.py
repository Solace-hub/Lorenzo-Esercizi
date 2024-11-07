from abc import ABC, abstractmethod

class PersonaleCucina(ABC):
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    @abstractmethod
    def lavora(self):
        pass


class Chef(PersonaleCucina):
    def __init__(self, nome, età, specialità):
        super().__init__(nome, età)
        self.specialità = specialità  # Aggiunta la specialità (tipo di cucina)

    
    def prepara_menu(self):
        print(f"{self.nome}, specializzato in {self.specialità}, sta preparando un nuovo menù.")

    
    def lavora(self):
        print(f"{self.nome}, Chef, sta preparando i piatti del menù.")
        

class SousChef(PersonaleCucina):
    def __init__(self, nome, età):
        super().__init__(nome, età)
        self.inventario = {}  

    
    def gestisci_inventario(self, ingrediente, quantità):
        if ingrediente in self.inventario:
            self.inventario[ingrediente] += quantità
        else:
            self.inventario[ingrediente] = quantità
        print(f"{self.nome} ha aggiornato l'inventario: {ingrediente} - {self.inventario[ingrediente]}")

    
    def lavora(self):
        print(f"{self.nome}, SousChef, sta assistendo lo Chef e gestendo l'inventario.")
        

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, età):
        super().__init__(nome, età)

    
    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} sta cucinando il piatto {nome_piatto}.")

    
    def lavora(self):
        print(f"{self.nome}, CuocoLinea, sta preparando i piatti nella linea di produzione.")



#Esempi
chef = Chef("Giovanni", 45, "cucina italiana")
sous_chef = SousChef("Lucia", 38)
cuoco_linea = CuocoLinea("Marco", 30)

chef.lavora() 
chef.prepara_menu()  

sous_chef.lavora() 
sous_chef.gestisci_inventario("pomodoro", 50)  
cuoco_linea.lavora() 
cuoco_linea.cucina_piatto("Spaghetti alla Carbonara") 
