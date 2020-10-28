import numpy as np

#Funcion que calcula la matriz resultante C despues de aplicar la operacion convolucion de A*B
def convolucion(A, B):
    C_filas = len(A) - len(B) + 1
    C_columnas = len(A[0]) - len(B[0]) + 1
    C = np.zeros((C_filas, C_columnas))
    for i in range(len(C)):
        for j in range(len(C[0])):
            suma = 0
            for n in range(len(B)):
                for m in range(len(B[0])):
                    suma += A[n + i][m + j] * B[n][m]
            C[i][j] = suma
    return C

Matriz1 = [[6, 9, 0, 3], [8, 4, 9, 1], [4, 1, 3, 12], [3, 2, 1, 100]]
Filtro = [[1, 0, 2], [5, 0, 9], [6, 2, 1]]

A = np.array(Matriz1)
B = np.array(Filtro)

print('Ejemplo 1')
print(convolucion(A, B))

print('\nEjemplo 2')

Matriz2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [0, 0, 1, 16, 17, 18] ,[0, 1, 0, 7, 23, 24], [1, 7, 6, 5, 4, 3]]
Filtro2 = [[1, 1, 1], [0, 0, 0], [2, 10, 3]]

A2 = np.array(Matriz2)
B2 = np.array(Filtro2)

print(convolucion(A2, B2))
