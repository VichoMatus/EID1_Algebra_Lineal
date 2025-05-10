#Clase Determinante con sus propios métodos

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada.")
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    det = 0
    for j in range(n):
        submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
        cofactor = ((-1) ** j) * matriz[0][j] * determinante(submatriz)
        det += cofactor
    return det