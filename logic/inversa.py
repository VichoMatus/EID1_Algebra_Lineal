#Clase Inversa con sus propios métodos
#Por matriz adjunta


def inversa(matriz):

    n = len(matriz)

    # Verificar que la matriz sea cuadrada
    if any(len(row) != n for row in matriz):
        raise ValueError("La matriz debe ser cuadrada.")

    # Crear matriz aumentada: [A | I]
    aumentada = [row[:] + [float(i == j) for j in range(n)] for i, row in enumerate(matriz)]

    # Aplicar eliminación Gauss-Jordan
    for i in range(n):
        # Pivote no nulo
        if aumentada[i][i] == 0:
            # Buscar una fila abajo para intercambiar
            for j in range(i + 1, n):
                if aumentada[j][i] != 0:
                    aumentada[i], aumentada[j] = aumentada[j], aumentada[i]
                    break
            else:
                raise ValueError("La matriz no es invertible (pivote cero).")

        # Hacer el pivote 1
        pivot = aumentada[i][i]
        aumentada[i] = [x / pivot for x in aumentada[i]]

        # Hacer ceros en las demás filas
        for j in range(n):
            if j != i:
                factor = aumentada[j][i]
                aumentada[j] = [a - factor * b for a, b in zip(aumentada[j], aumentada[i])]

    # Extraer la parte derecha (inversa)
    inversa = [row[n:] for row in aumentada]

    return inversa

