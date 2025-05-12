def determinante(matriz, nivel=0):
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada.")

    indent = "    " * nivel
    n = len(matriz)

    if n == 1:
        return matriz[0][0], f"{indent}Determinante de 1x1: {matriz[0][0]}\n"

    if n == 2:
        det = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        pasos = f"{indent}Determinante 2x2: {matriz[0][0]}*{matriz[1][1]} - {matriz[0][1]}*{matriz[1][0]} = {det}\n"
        return det, pasos

    det = 0
    pasos = f"{indent}Expandiendo por la primera fila:\n"
    for j in range(n):
        submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
        signo = (-1) ** j
        minor_det, minor_pasos = determinante(submatriz, nivel + 1)
        cofactor = signo * matriz[0][j] * minor_det
        pasos += f"{indent}Cofactor A[0][{j}]: {signo}*{matriz[0][j]}*Det(submatriz) = {cofactor}\n"
        pasos += minor_pasos
        det += cofactor

    pasos += f"{indent}Determinante total = {det}\n"
    return det, pasos
