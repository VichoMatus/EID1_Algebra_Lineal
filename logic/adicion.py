def suma_matrices(A, B):
    pasos = "Paso 1: Sumar elementos correspondientes de A y B\n\n"
    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            suma = A[i][j] + B[i][j]
            pasos += f"A[{i}][{j}] + B[{i}][{j}] = {A[i][j]} + {B[i][j]} = {suma}\n"
            fila.append(suma)
        resultado.append(fila)

    return resultado, pasos
