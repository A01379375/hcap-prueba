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

C = np.zeros((2, 2))

print(A)

print(A[1][0])

print(C)

print(convolucion(A, B))
