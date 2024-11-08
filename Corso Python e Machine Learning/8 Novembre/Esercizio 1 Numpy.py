import numpy as np

array = np.arange(10, 49)
print(array.dtype)
print(array.shape)

array.astype(np.float64)
print(array.dtype)
print(array.shape)