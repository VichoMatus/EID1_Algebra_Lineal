#Clase Inversa con sus propios métodos

def matriz_inversa(matrix):
    """
    Calcula la inversa de una matriz cuadrada utilizando el método de Gauss-Jordan.
    No utiliza NumPy.
    """
    n = len(matrix)
    # Verifica que sea cuadrada
    if any(len(row) != n for row in matrix):
        raise ValueError("La matriz debe ser cuadrada para calcular su inversa.")

    # Crear la matriz identidad
    identity = [[float(i == j) for j in range(n)] for i in range(n)]

    # Crear una copia extendida de la matriz con la identidad al lado (A | I)
    for i in range(n):
        matrix[i] = matrix[i] + identity[i]

    # Aplicar eliminación Gauss-Jordan
    for i in range(n):
        # Pivote principal
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("La matriz no es invertible (pivote cero).")

        # Normalizar la fila del pivote
        for j in range(2 * n):
            matrix[i][j] /= pivot

        # Eliminar otras filas
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(2 * n):
                    matrix[k][j] -= factor * matrix[i][j]

    # Extraer la parte derecha como inversa (I | A^-1)
    inversa = [row[n:] for row in matrix]
    return inversa
