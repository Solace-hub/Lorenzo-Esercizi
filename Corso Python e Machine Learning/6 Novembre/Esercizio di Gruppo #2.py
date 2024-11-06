from abc import ABC, abstractmethod

#Classe Astratta e Attributi Privati
class Veicolo(ABC):
    def __init__(self, marca, modello, anno):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False

    #Metodo per accendere il veicolo
    def accendi(self):
        if not self.__accensione:
            self.__accensione = True
            print(f"{self.__marca} {self.__modello} acceso")
        else:
            print(f"{self.__marca} {self.__modello} è già acceso")

    #Metodo per spegnere il veicolo
    def spegni(self):
        if self.__accensione:
            self.__accensione = False
            print(f"{self.__marca} - {self.__modello} spento")
        else:
            print(f"{self.__marca} - {self.__modello} è già spento")

    #Restituisce i dettagli del veicolo
    def get_dettagli(self):
        return (f"Marca: {self.__marca}, Modello: {self.__modello}, Anno: {self.__anno}")

    #Metodo astratto che deve essere implementato dalle sottoclassi
    def metodo_specifico(self):
        pass
