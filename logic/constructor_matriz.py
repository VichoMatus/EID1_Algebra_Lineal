import numpy as np

def build_matrix_from_input(rows: int, cols: int, values: list):
    if len(values) != rows * cols:
        raise ValueError("Cantidad de valores no coincide con dimensiones.")
    return np.array(values).reshape((rows, cols))
