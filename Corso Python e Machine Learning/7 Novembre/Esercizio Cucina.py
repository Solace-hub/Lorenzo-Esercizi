#Crea una classe ristorante con una lista di liste chiamata menu e una lista chiamata ordinazione,
#Nel menu ci devono essere X piatti composti ogniuno da una lista propria di ingredienti, 
#e la lista ordinazione invece e composta dalle singole ordinazioni del cleinte, 
#Servirrà quindi una classe cliente e ogni membro della cucina potrà servire solo X piatti
#EXTRA: aggiungi personale, budget e costi, Feedback piatti e chef

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



#///



class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.ordinazione = []

    def aggiungi_ordinazione(self, piatto):
        self.ordinazione.append(piatto)

    def visualizza_ordinazione(self):
        print(f"L'ordinazione di {self.nome} è: {', '.join(self.ordinazione)}")




class Ristorante:
    def __init__(self, nome, budget, costi):
        self.nome = nome
        self.menu = []
        self.ordinazioni = []
        self.personale = []
        self.budget = budget
        self.costi = costi
        self.feedback = {}

    def aggiungi_piatto_menu(self, piatto, ingredienti):
        self.menu.append([piatto, ingredienti])

    def aggiungi_ordinazione(self, cliente, ordinazione):
        self.ordinazioni.append((cliente, ordinazione))

    def aggiungi_personale(self, persona):
        self.personale.append(persona)

    def fornisci_feedback(self, piatto, feedback):
        if piatto in self.feedback:
            self.feedback[piatto].append(feedback)
        else:
            self.feedback[piatto] = [feedback]

    def visualizza_menu(self):
        print(f"Menù del Ristorante {self.nome}:")
        for piatto, ingredienti in self.menu:
            print(f"- {piatto}: {', '.join(ingredienti)}")

    def servire_ordinazioni(self):
        for cliente, ordinazione in self.ordinazioni:
            print(f"Servendo l'ordinazione di {cliente.nome}: {', '.join(ordinazione)}")
            for piatto in ordinazione:
                for persona in self.personale:
                    if isinstance(persona, CuocoLinea):
                        persona.cucina_piatto(piatto)
                    elif isinstance(persona, Chef):
                        persona.prepara_menu()
                    elif isinstance(persona, SousChef):
                        persona.gestisci_inventario(piatto, 1)
            print("Ordinazione servita!")



'''ristorante = Ristorante("Trattoria Italiana", 50000, 30000)

chef = Chef("Giovanni", 45, "cucina italiana")
sous_chef = SousChef("Lucia", 38)
cuoco_linea = CuocoLinea("Marco", 30)

ristorante.aggiungi_personale(Chef)
ristorante.aggiungi_personale(SousChef)
ristorante.aggiungi_personale(CuocoLinea)'''





