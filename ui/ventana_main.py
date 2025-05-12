import customtkinter as ctk
from tkinter import messagebox

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
        self.operation = ctk.StringVar(value="Determinante")

        # Inputs para dimensiones
        ctk.CTkLabel(root, text="Filas:").grid(row=0, column=0)
        self.filas_entry = ctk.CTkEntry(root, width=60)
        self.filas_entry.insert(0, "2")
        self.filas_entry.grid(row=0, column=1)

        ctk.CTkLabel(root, text="Columnas:").grid(row=0, column=2)
        self.columnas_entry = ctk.CTkEntry(root, width=60)
        self.columnas_entry.insert(0, "2")
        self.columnas_entry.grid(row=0, column=3)

        ctk.CTkButton(root, text="Generar matrices", command=self.generar_matrices).grid(row=0, column=4, padx=10)

        # Selección de operación
        ctk.CTkLabel(root, text="Operación:").grid(row=1, column=0)
        self.menu = ctk.CTkOptionMenu(root, variable=self.operation, values=["Suma", "Resta", "Multiplicación", "Determinante", "Inversa"])
        self.menu.grid(row=1, column=1, columnspan=2, pady=5)

        ctk.CTkButton(root, text="Calcular", command=self.calcular).grid(row=1, column=4)

        # Marcos para matrices
        self.matriz_a_frame = ctk.CTkFrame(root)
        self.matriz_a_frame.grid(row=2, column=1, padx=10, pady=5)

        self.matriz_b_frame = ctk.CTkFrame(root)
        self.matriz_b_frame.grid(row=2, column=2, padx=10, pady=5)

        self.resultado_frame = ctk.CTkFrame(root)
        self.resultado_frame.grid(row=2, column=3, padx=10, pady=5)

    def generar_matrices(self):
        # Borrar entradas anteriores
        for frame in [self.matriz_a_frame, self.matriz_b_frame, self.resultado_frame]:
            for widget in frame.winfo_children():
                widget.destroy()

        self.entries_a = []
        self.entries_b = []

        filas = int(self.filas_entry.get())
        columnas = int(self.columnas_entry.get())

        for i in range(filas):
            fila_a, fila_b = [], []
            for j in range(columnas):
                entry_a = ctk.CTkEntry(self.matriz_a_frame, width=50)
                entry_a.grid(row=i, column=j, padx=2, pady=2)
                fila_a.append(entry_a)

                entry_b = ctk.CTkEntry(self.matriz_b_frame, width=50)
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

        # Limpiar resultado anterior
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()

        try:
            if operacion == "Determinante":
                resultado = determinante(A)
                label = ctk.CTkLabel(self.resultado_frame, text=f"Determinante de A: {resultado:.2f}", font=("Arial", 14))
                label.grid(row=0, column=0, padx=10, pady=10)

            else:
                B = self.leer_matriz(self.entries_b)

                if operacion == "Suma":
                    resultado = suma_matrices(A, B)
                elif operacion == "Resta":
                    resultado = resta_matrices(A, B)
                elif operacion == "Multiplicación":
                    resultado = multiplicar_matrices(A, B)
                elif operacion == "Inversa":
                    resultado = inversa(A)
                else:
                    raise ValueError("Operación no implementada.")

                for i, fila in enumerate(resultado):
                    for j, val in enumerate(fila):
                        celda = ctk.CTkLabel(self.resultado_frame, text=f"{val:.2f}",
                                             width=60, height=30, fg_color="#343638", corner_radius=6)
                        celda.grid(row=i, column=j, padx=4, pady=4)

        except Exception as e:
            messagebox.showerror("Error", str(e))


def lanzar_ventana():
    ctk.set_appearance_mode("dark")  # o "light"
    ctk.set_default_color_theme("blue")  # o "green", "dark-blue"
    root = ctk.CTk()
    app = MatrixCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    lanzar_ventana()
