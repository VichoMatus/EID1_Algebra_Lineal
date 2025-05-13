def lu_factorizacion(matriz):
    n = len(matriz)
    A = [row[:] for row in matriz]
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    P = [[float(i == j) for j in range(n)] for i in range(n)]
    pasos = "=== Factorización LU ===\n\n"

    for k in range(n):
        # Calcular los multiplicadores y actualizar la matriz A para obtener U
        if A[k][k] == 0:
            break # Factorización sin pivotamiento falla si el pivote es cero
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            L[i][k] = factor
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
        L[k][k] = 1.0
        L[k][k] = 1.0
        print(f"Paso {k}: L[{k}][{k}] = {L[k][k]}")
        for j in range(k, n):
            U[k][j] = A[k][j]

        pasos += f"\nPaso {k+1}:\n"
        pasos += f"Matriz L:\n" + '\n'.join(['  ' + '  '.join(f"{val:6.2f}" for val in fila) for fila in L]) + "\n"
        pasos += f"Matriz U:\n" + '\n'.join(['  ' + '  '.join(f"{val:6.2f}" for val in fila) for fila in U]) + "\n"

    pasos += "\n✅ Resultado final:\n"
    pasos += "Matriz P:\n" + '\n'.join(['  ' + '  '.join(f"{val:6.2f}" for val in fila) for fila in P]) + "\n"
    pasos += "Matriz L:\n" + '\n'.join(['  ' + '  '.join(f"{val:6.2f}" for val in fila) for fila in L]) + "\n"
    pasos += "Matriz U:\n" + '\n'.join(['  ' + '  '.join(f"{val:6.2f}" for val in fila) for fila in U]) + "\n"

    return P, L, U, pasos
