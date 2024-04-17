#Importar Numpy
import numpy as np
#Crear una matriz cuadrada "a" de dos dimensiones
a=np.array([[6,9],[3,7]])
#usando la funcion linalg.eig buscamos los valores y vectores propios
#Y se los asignamos a vectores_p y valores_p
vectores_p, valores_p =np.linalg.eig(a)
print(a)
print(vectores_p)
print(valores_p)