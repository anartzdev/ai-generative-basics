import numpy as np

# Crea una matriz con los números del 1 al 9
mat = np.array([[1, 2, 1], [2, 1, 2], [4, 5, 6]])

# Calcula la suma de todos los elementos
suma = np.sum(mat[0, :])

print(suma)  # Output: 55