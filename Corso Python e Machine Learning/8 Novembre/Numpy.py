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

#//


arr_2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(arr_2d[1:3])
print(arr_2d[:, 1:3])
print(arr_2d[1:, 1:3])


#array[start:stop:step] Slicing  Start inclusivo, stop esclusivo, step tra un indice e l'altro

print(arr[2:7]) #base
print(arr[1:8:2]) #con passo
print(arr[:5]) #start
print(arr[5:]) #stop
print(arr[-5:]) #negativi

#Fancy indexing
arr = np.array([10, 20, 30, 40, 50])

indices = np.array([1, 3])
print(arr[indices])

indices = [0,2,4]
print(arr[indices])


