<<<<<<< Updated upstream
=======
import customtkinter as ctk
from tkinter import messagebox

from logic.sustraccion import resta_matrices
from logic.adicion import suma_matrices
from logic.determinante import determinante
from logic.multiplicacion import multiplicar_matrices
from logic.inversa import inversa
from logic.lu_factorizacion import lu_factorizacion


class MatrixTab:
    def __init__(self, parent, operation):
        self.operation = operation
        self.entries_a = []
        self.entries_b = []

        # --- CONTENEDOR PRINCIPAL ---
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        # --- Entradas de dimensiones ---
        ctk.CTkLabel(self.frame, text="Filas:").grid(row=0, column=0)
        self.filas_entry = ctk.CTkEntry(self.frame, width=60)
        self.filas_entry.insert(0, "2")
        self.filas_entry.grid(row=0, column=1)

        ctk.CTkLabel(self.frame, text="Columnas:").grid(row=0, column=2)
        self.columnas_entry = ctk.CTkEntry(self.frame, width=60)
        self.columnas_entry.insert(0, "2")
        self.columnas_entry.grid(row=0, column=3)

        ctk.CTkButton(self.frame, text="Generar matrices", command=self.generar_matrices).grid(row=0, column=4, padx=10)
        ctk.CTkButton(self.frame, text="Calcular", command=self.calcular).grid(row=1, column=4)

        # --- Marcos para matrices y resultado ---
        self.matriz_a_frame = ctk.CTkFrame(self.frame)
        self.matriz_a_frame.grid(row=1, column=1, padx=10, pady=10)

        self.matriz_b_frame = ctk.CTkFrame(self.frame)
        self.matriz_b_frame.grid(row=1, column=2, padx=10, pady=10)

        self.resultado_frame = ctk.CTkFrame(self.frame)
        self.resultado_frame.grid(row=1, column=3, padx=10, pady=10)

        self.pasos_textbox = ctk.CTkTextbox(self.frame, width=400, height=200)
        self.pasos_textbox.grid(row=3, column=0, columnspan=5, padx=10, pady=10)


        # Etiquetas
        ctk.CTkLabel(self.frame, text="Matriz A").grid(row=2, column=1)
        if operation in ["Suma", "Resta", "Multiplicación"]:
            ctk.CTkLabel(self.frame, text="Matriz B").grid(row=2, column=2)
        ctk.CTkLabel(self.frame, text="Resultado").grid(row=2, column=3)

    def generar_matrices(self):
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

                if self.operation in ["Suma", "Resta", "Multiplicación"]:
                    entry_b = ctk.CTkEntry(self.matriz_b_frame, width=50)
                    entry_b.grid(row=i, column=j, padx=2, pady=2)
                    fila_b.append(entry_b)

            self.entries_a.append(fila_a)
            if self.operation in ["Suma", "Resta", "Multiplicación"]:
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
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()
        self.pasos_textbox.delete("0.0", "end")  # limpia pasos anteriores

        try:
            A = self.leer_matriz(self.entries_a)

            if self.operation == "Determinante":
                if len(A) != len(A[0]):
                    raise ValueError("La matriz debe ser cuadrada para calcular el determinante.")
                resultado, pasos = determinante(A)
                ctk.CTkLabel(self.resultado_frame, text=f"Determinante de A: {resultado:.2f}",
                            font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)

            elif self.operation == "Inversa":
                if len(A) != len(A[0]):
                    raise ValueError("La matriz debe ser cuadrada para calcular su inversa.")
                resultado, pasos = inversa(A)
                self.mostrar_matriz(resultado)

            elif self.operation == "LU":
                if len(A) != len(A[0]):
                    raise ValueError("La matriz debe ser cuadrada para realizar la factorización LU.")
                P, L, U, pasos = lu_factorizacion(A)
                # Mostrar las matrices P, L y U en el resultado_frame
                ctk.CTkLabel(self.resultado_frame, text="Matriz P:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=0)
                self.mostrar_matriz(P, start_row=1)

                ctk.CTkLabel(self.resultado_frame, text="Matriz L:", font=("Arial", 12)).grid(row=len(P)+1, column=0, padx=10, pady=0)
                self.mostrar_matriz(L, start_row=len(P)+2)

                ctk.CTkLabel(self.resultado_frame, text="Matriz U:", font=("Arial", 12)).grid(row=len(P)+len(L)+2, column=0, padx=10, pady=0)
                self.mostrar_matriz(U, start_row=len(P)+len(L)+3)


            else:
                B = self.leer_matriz(self.entries_b)
                if self.operation == "Suma":
                    resultado, pasos = suma_matrices(A, B)
                elif self.operation == "Resta":
                    resultado, pasos = resta_matrices(A, B)
                elif self.operation == "Multiplicación":
                    resultado, pasos = multiplicar_matrices(A, B)
                else:
                    raise ValueError("Operación no válida")
                self.mostrar_matriz(resultado)

            self.pasos_textbox.insert("0.0", pasos)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_matriz(self, resultado, start_row= 0):
        for i, fila in enumerate(resultado):
            for j, val in enumerate(fila):
                ctk.CTkLabel(self.resultado_frame, text=f"{val:.2f}",
                             width=60, height=30, fg_color="#b2bac2", corner_radius=6).grid(row=i + start_row, column=j, padx=4, pady=4)


def run_app():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("950x750")
    app.title("Calculadora de Matrices")

    tabview = ctk.CTkTabview(app)
    tabview.pack(fill="both", expand=True, padx=20, pady=20)

    # Crear pestañas y asignarles instancias de MatrixTab
    tabs = {
        "Suma": tabview.add("Suma"),
        "Resta": tabview.add("Resta"),
        "Multiplicación": tabview.add("Multiplicación"),
        "Inversa": tabview.add("Inversa"),
        "Determinante": tabview.add("Determinante"),
        "LU": tabview.add("LU")
    }

    for operacion, contenedor in tabs.items():
        MatrixTab(contenedor, operacion)

    app.mainloop()

>>>>>>> Stashed changes
