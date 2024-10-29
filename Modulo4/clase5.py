"""
USO DE LIBRERIA NUMPY
"""

import numpy as np

# Podemos crear una lista 
# En este caso con una secuencia del 1 al 10, pero sin separar por comas
np_lista = np.arange(1, 10)
print(np_lista)
# Para separar cada elemento por comas lo convertimos en una lista normal
print(list(np_lista))

# Podemos organizar una lista tipo una matriz
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(lista)
print(matriz)

# Podemos sumar matrices
sumar_matrices = matriz[0] + matriz[1]
print(sumar_matrices)

# Podemos sumar un valor especifico de las matrices
# El primer numero de indice seria la primera lista
# Y el segundo numero de indice seria el valor de esa lista
# Osea en este caso sumo el 1 + 6
sumar_valor = matriz[0,0] + matriz[1,2]
print(sumar_valor)

# Podemos hacer calculos estadisticos
data = [12, 20, 21, 11, 15, 19, 27]
# Promedio
promedio = np.mean(data)
print("Promedio: ", promedio)

# Desviacion estandar
desviacion = np.std(data)
print("Desviacion: ", desviacion)

# Numero maximo y su indice en la lista
maximo = np.max(data)
indice = np.argmax(data)
print(f"El maximo es {maximo} y su indice es {indice}")