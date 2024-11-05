#Decoratore 1 asterisco diventa tupla, è un placeholder
'''def funzione(*argomenti):
    for arg in argomenti:
        print(arg)

funzione(11,2,4)'''

#Decoratore con 2 asterischi diventa dizionario, è un placeholder

'''def funzione(**argomenti):
    print(type(argomenti))

funzione(num1 = 11, num2= 2, num3 = 4)'''


'''def funzione (a,b):
    somma = a+b
    return somma

variabile = funzione(10,11)
print(funzione(variabile, 10))'''


'''def funzione ():
    global variabile1  #Global serve a globalizzare una variabile locale
    variabile1 = 11

    print(variabile1)
    funzione()
    print(variabile1)'''


def triplica(a):
    return a*3
lista = [1,2,3,4,5]

listaT= []

for num in lista:
    listaT.append(triplica(num))

    