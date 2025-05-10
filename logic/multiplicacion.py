#Clase multiplicación con sus propios métodos

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimensiones incompatibles para multiplicación.")
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = sum(A[i][k] * B[k][j] for k in range(len(B)))
            fila.append(suma)
        resultado.append(fila)
    return resultado