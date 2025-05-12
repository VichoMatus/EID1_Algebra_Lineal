import tkinter as tk
from tkinter import ttk, messagebox

from logic.sustraccion import resta_matrices
from logic.adicion import suma_matrices
from logic.determinante import determinante
from logic.multiplicacion import multiplicar_matrices
from logic.inversa import inversa

class MatrixCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices")

        self.entries_a = []
        self.entries_b = []
        self.operation = tk.StringVar(value="Determinante")

        # Inputs para dimensiones
        ttk.Label(root, text="Filas:").grid(row=0, column=0)
        self.filas_entry = ttk.Spinbox(root, from_=1, to=4, width=5)
        self.filas_entry.grid(row=0, column=1)

        ttk.Label(root, text="Columnas:").grid(row=0, column=2)
        self.columnas_entry = ttk.Spinbox(root, from_=1, to=4, width=5)
        self.columnas_entry.grid(row=0, column=3)

        ttk.Button(root, text="Generar matrices", command=self.generar_matrices).grid(row=0, column=4)

        # Selección de operación
        ttk.Label(root, text="Operación:").grid(row=1, column=0)
        self.menu = ttk.OptionMenu(root, self.operation, "Determinante", "Suma", "Resta", "Multiplicación", "Determinante", "Inversa")
        self.menu.grid(row=1, column=1, columnspan=2)

        ttk.Button(root, text="Calcular", command=self.calcular).grid(row=1, column=4)

        # Marcos para matrices
        self.matriz_a_frame = tk.LabelFrame(root, text="Matriz A")
        self.matriz_a_frame.grid(row=2, column=1, rowspan=5, padx=10, pady=5)

        self.matriz_b_frame = tk.LabelFrame(root, text="Matriz B")
        self.matriz_b_frame.grid(row=2, column=2, rowspan=5, padx=10, pady=5)

        self.resultado_frame = tk.LabelFrame(root, text="Resultado")
        self.resultado_frame.grid(row=2, column=3, rowspan=5, padx=10, pady=5)


    def generar_matrices(self):
        # Borrar entradas anteriores
        for widget in self.matriz_a_frame.winfo_children():
            widget.destroy()
        for widget in self.matriz_b_frame.winfo_children():
            widget.destroy()
        self.entries_a = []
        self.entries_b = []

        filas = int(self.filas_entry.get())
        columnas = int(self.columnas_entry.get())

        for i in range(filas):
            fila_a, fila_b = [], []
            for j in range(columnas):
                entry_a = tk.Entry(self.matriz_a_frame, width=5)
                entry_a.grid(row=i, column=j, padx=2, pady=2)
                fila_a.append(entry_a)

                entry_b = tk.Entry(self.matriz_b_frame, width=5)
                entry_b.grid(row=i, column=j, padx=2, pady=2)
                fila_b.append(entry_b)

            self.entries_a.append(fila_a)
            self.entries_b.append(fila_b)

    def leer_matriz(self, entries):
        matriz = []
        for fila in entries:
            valores = []
            for celda in fila:
                try:
                    valores.append(float(celda.get()))
                except ValueError:
                    valores.append(0)
            matriz.append(valores)
        return matriz

    def calcular(self):
        operacion = self.operation.get()
        A = self.leer_matriz(self.entries_a)

        # Limpiar contenido anterior del resultado
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()

        try:
            if operacion == "Determinante":
                resultado = determinante(A)
                # Mostrar resultado como texto
                tk.Label(self.resultado_frame, text=f"Determinante de A: {resultado:.2f}",
                        font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)

            else:
                B = self.leer_matriz(self.entries_b)

                if operacion == "Suma":
                    resultado = suma_matrices(A, B)
                elif operacion == "Resta":
                    resultado = resta_matrices(A, B)
                elif operacion == "Multiplicación":
                    resultado = multiplicar_matrices(A, B)
                elif operacion == "Inversa":
                    resultado == inversa(A)
                else:
                    raise ValueError("Operación no implementada.")

                # Mostrar resultado como tabla
                for i, fila in enumerate(resultado):
                    for j, val in enumerate(fila):
                        celda = tk.Label(self.resultado_frame, text=f"{val:.2f}", width=6,
                                        borderwidth=1, relief="solid", font=("Arial", 10))
                        celda.grid(row=i, column=j, padx=2, pady=2)

        except Exception as e:
            # Mostrar errores como alerta
            messagebox.showerror("Error", str(e))


def lanzar_ventana():
    root = tk.Tk()
    app = MatrixCalculatorGUI(root)
    root.mainloop()
       

if __name__ == "__main__":
    lanzar_ventana()