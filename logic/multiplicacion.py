def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimensiones incompatibles para multiplicación.")

    pasos = "Paso 1: Multiplicar filas de A por columnas de B\n\n"
    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            detalle = f"C[{i}][{j}] = "
            for k in range(len(B)):
                producto = A[i][k] * B[k][j]
                suma += producto
                detalle += f"A[{i}][{k}]*B[{k}][{j}] ({A[i][k]}*{B[k][j]}) + "
            detalle = detalle.rstrip("+ ") + f"= {suma}"
            pasos += detalle + "\n"
            fila.append(suma)
        resultado.append(fila)

    return resultado, pasos
