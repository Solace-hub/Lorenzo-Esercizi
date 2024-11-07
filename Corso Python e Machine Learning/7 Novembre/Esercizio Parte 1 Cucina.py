# creare una classe base PersonaleCucina e diverse classi derivate che rappresentano differenti ruoli all'interno della cucina di un ristorante. 
# L'obiettivo è di utilizzare l'ereditarietà per condividere alcune caratteristiche comuni 
# mentre si distinguono le responsabilità e le azioni specifiche di ogni ruolo.
#Classe PersonaleCucina:
#Attributi:
#nome (stringa)
#età (intero)
#Metodi:
#lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)
#Classi Derivate:
#Chef:
#Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
#Metodi come prepara_menu() che dettaglia come lo chef crea nuovi piatti e menu
#SousChef:
#Metodi come gestisci_inventario() per gestire l'inventario della cucina e assistere lo chef
#CuocoLinea:
#Metodi come cucina_piatto(nome_piatto) che specifica la preparazione di un piatto specifico nella linea di produzione






class PersonaleCucina:
    def __init__(self, nome, età):
        self.__nome = nome
        self.__età = età
        self.__ingredienti = []

    def get_nome(self):
        return self.__nome
    
    def get_età(self):
        return self.__età
    
    def lavora(self):
        print(f"{self.__nome} sta lavorando in cucina")
        
class Chef(PersonaleCucina):
    def __init__(self, nome, età, specialità):
        super().__init__(nome, età)
        self.__specialità = specialità
    
    def get_specialità(self):
        return self.__specialità
    
    def prepara_menù(self):
        print(f"{self.__nome}, specializzato in {self.__specialità}, sta preparando un nuovo menù")


class SousChef(PersonaleCucina):
    def gestisci_inventario(self):
        print(f"{self.__nome} sta gestendo l'inventario della cucina.")


class CuocoLinea(PersonaleCucina):
    def cucina_piatto(self, nome_piatto):
        print(f"{self.__nome} sta cucinando il piatto {nome_piatto}.")