def inversa(matriz):
    n = len(matriz)
    pasos = "=== Método de Gauss-Jordan para obtener la matriz inversa ===\n\n"

    if any(len(row) != n for row in matriz):
        raise ValueError("La matriz debe ser cuadrada.")

    # Crear matriz aumentada: [A | I]
    aumentada = [row[:] + [float(i == j) for j in range(n)] for i, row in enumerate(matriz)]
    
    pasos += "Paso 1: Formamos la matriz aumentada [A | I]\n"
    for fila in aumentada:
        pasos += "  " + "  ".join(f"{val:6.2f}" for val in fila) + "\n"
    pasos += "\n"

    for i in range(n):
        if aumentada[i][i] == 0:
            for j in range(i + 1, n):
                if aumentada[j][i] != 0:
                    aumentada[i], aumentada[j] = aumentada[j], aumentada[i]
                    pasos += f"→ Intercambiamos fila {i+1} con fila {j+1} para obtener un pivote distinto de 0.\n"
                    break
            else:
                raise ValueError("La matriz no es invertible (pivote cero).")

        pivote = aumentada[i][i]
        aumentada[i] = [x / pivote for x in aumentada[i]]
        pasos += f"\nPaso 2.{i+1}: Normalizamos fila {i+1} dividiendo entre el pivote {pivote:.2f}\n"
        pasos += "  " + "  ".join(f"{val:6.2f}" for val in aumentada[i]) + "\n"

        for j in range(n):
            if j != i:
                factor = aumentada[j][i]
                fila_original = aumentada[j][:]
                aumentada[j] = [a - factor * b for a, b in zip(aumentada[j], aumentada[i])]
                pasos += f"\nPaso 3.{i+1}.{j+1}: Restamos {factor:.2f} × fila {i+1} a fila {j+1} para hacer cero en la posición ({j+1},{i+1})\n"
                pasos += "  " + "  ".join(f"{val:6.2f}" for val in aumentada[j]) + "\n"

    pasos += "\n✅ Paso final: Extraemos la parte derecha de la matriz aumentada, que es la inversa de A.\n"
    inversa = [fila[n:] for fila in aumentada]
    for fila in inversa:
        pasos += "  " + "  ".join(f"{val:6.2f}" for val in fila) + "\n"

    return inversa, pasos
