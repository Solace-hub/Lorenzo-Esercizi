import numpy as np
'''#Punto 1 20 numeri casuali tra 10 e 50
array = np.random.randint(10,51,20)
print(array)
#Punto 2 
primi_dieci_elementi = array[:10]
print(primi_dieci_elementi)
#Punto 3
ultimi_cinque_elementi = array[-5:]
#Punto 4
tra_cinque_e_quindici = array[5:15]
#Punto 5
ogni_terzo_elemento = array[::3]
print(ogni_terzo_elemento)
#Punto 6
valore_99 = array[5:10] = 99
print(valore_99)
#Punto 7
print(array, primi_dieci_elementi, ultimi_cinque_elementi, tra_cinque_e_quindici, ogni_terzo_elemento, valore_99)'''



class OperazioniArray:
    def __init__ (self):
        self.array = np.random.randint(10, 51, 20)

    def primi_dieci_elementi(self):
        return self.array[:10]
    
    def ultimi_cinque_elementi(self):
        return self.array[-5:]
    
    def tra_cinque_e_quindici(self):
        return self.array[5:15]
    
    def ogni_terzo_elemento(self):
        return self.array[::3]
    
    def valore_99(self):
         self.array[5:10] = 99
         return self.array
    
    def stampa_tutto(self):
        print("Array originale:", self.array)
        print("Primi 10 elementi:", self.primi_dieci_elementi())
        print("Ultimi 5 elementi:", self.ultimi_cinque_elementi())
        print("Elementi dall'indice 5 all'indice 15:", self.tra_cinque_e_quindici())
        print("Ogni terzo elemento:", self.ogni_terzo_elemento())
        print("Valore 99:", self.valore_99())


array1 = OperazioniArray()
array1.stampa_tutto()
