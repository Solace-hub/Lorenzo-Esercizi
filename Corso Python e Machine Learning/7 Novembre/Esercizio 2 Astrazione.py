from abc import ABC, abstractmethod


class Operaio(ABC):
    @abstractmethod
    def esegui_lavoro(self):
        pass


class Muratore(ABC):
    @abstractmethod
    def costruisci_muri(self):
        pass


class Elettricista(ABC):
    @abstractmethod
    def installa_impianto(self):
        pass


class ElettricistaSpecializzato(Operaio, Elettricista):
    def esegui_lavoro(self):
        pass

    def installa_impianto(self):
        pass


class MuratoreSpecializzato(Operaio, Muratore):
    def esegui_lavoro(self):
        pass

    def costruisci_muri(self):
        pass
