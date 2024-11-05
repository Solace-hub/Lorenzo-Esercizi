#Definiamo la funzione creando le due variabili x e y
def fibonacci(n):
    x,y = 0,1
    #La lista vuota serve a permetterci di memorizzare la sequenza successivamente
    sequenza_fibonacci = []
    #Finché x è minore o uguale a N, la sequenza va avanti aggiungendo e sommando il numero precedente al successivo
    while x <= n:
        sequenza_fibonacci.append(x)
        x,y = y, x + y
        return sequenza_fibonacci
    
n = int(input("Inserisci un numero: "))
#Incapsuliamo il tutto nella variabile
sequenza_di_fibonacci = fibonacci(n)
print("Questa è la sequenza di Fibonacci fino a", n, sequenza_di_fibonacci)

def fibonacci():
    pass
