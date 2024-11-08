import numpy as np

#Creazione di un array undimensionale

arr = np.array([1,2,3], [4,5,6])

#Creazione di un array bidimensionale

arr2d = np.array([[1,2,3], [4,5,6]])

#arange

arr = np.arange(10)
print(arr)

#reshape

arr = np.arange(6)
reshaped_arr = arr.reshape((6,1))
print(reshaped_arr)

