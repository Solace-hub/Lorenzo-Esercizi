import numpy as np

#Es1
''''array_1d = np.random.random(10)  

array_2d = np.random.randint(0, 11, (3, 3))

print("Array 1d:", array_1d)
print("Array 2d:", array_2d)
'''

#Es2
'''array1 = np.random.randint(0, 11, (4, 4))
array2 = np.random.randint(0, 11, (4, 4))

somma_array1 = np.sum(array1[-1, 1:])
somma_array2 = np.sum(array2[-1, 1:])

array_unito = np.concatenate((array1, array2), axis=1)

print("Array 1:", array1)
print("Array 2:", array2)
print("Somma Array 1 ultima riga, seconda colonna", somma_array1)
print("Somma Array 2 ultima riga, seconda colonna", somma_array2)
print("Array Unito asse 1", array_unito)'''

#Es3

import numpy as np
from scipy import stats

array1d= np.random.randint(1, 1000, 50)

media = np.mean(array1d)

moda = stats.mode(array1d).mode

deviazione_standard = np.std(array1d)

array_5x10 = array1d.reshape(5, 10)

print("Array 1d", array1d)
print("Media:", media)
print("Moda:", moda)
print("Deviazione standard:", deviazione_standard)
print("Array trasformato in 5x10:\n", array_5x10)
