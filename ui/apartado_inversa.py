import customtkinter as ctk
from logic.constructor_matriz import build_matrix_from_input
from logic.inversa import matriz_inversa

def setup_inverse_tab(tab_inversa):
    # Frame general con dos columnas (izquierda: entrada, derecha: resultado)
    content_frame = ctk.CTkFrame(tab_inversa)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    left_frame = ctk.CTkFrame(content_frame)
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    right_frame = ctk.CTkFrame(content_frame)
    right_frame.pack(side="right", fill="both", expand=True)

    # ---- FRAME IZQUIERDO (entrada de matriz) ----
    # Subframe para campos de dimensiones
    dim_frame = ctk.CTkFrame(left_frame)
    dim_frame.pack(fill="x", pady=(10, 0))

    ctk.CTkLabel(dim_frame, text="Filas:").pack(side="left", padx=(0, 5))
    rows_entry = ctk.CTkEntry(dim_frame, width=50)
    rows_entry.pack(side="left", padx=(0, 15))

    ctk.CTkLabel(dim_frame, text="Columnas:").pack(side="left", padx=(0, 5))
    cols_entry = ctk.CTkEntry(dim_frame, width=50)
    cols_entry.pack(side="left", padx=(0, 15))

    # Botón para generar la matriz
    generate_btn = ctk.CTkButton(left_frame, text="Generar Matriz")
    generate_btn.pack(pady=10)

    # Etiqueta de error
    error_label = ctk.CTkLabel(left_frame, text="", text_color="red")
    error_label.pack(pady=(0, 5))

    # Frame para mostrar la grilla de entradas
    matrix_frame = ctk.CTkFrame(left_frame)
    matrix_frame.pack(pady=10)

    # ---- FRAME DERECHO (resultado) ----
    calculate_btn = ctk.CTkButton(right_frame, text="Calcular Inversa", state="disabled")
    calculate_btn.pack(pady=10)

    result_container = ctk.CTkFrame(right_frame)
    result_container.pack(expand=True)

    result_label = ctk.CTkLabel(result_container, text="", justify="center")
    result_label.pack(expand=True)

    # Lista para guardar referencias a los CTkEntry de la matriz
    entries = []
    current_rows = 0
    current_cols = 0

    # Función para generar la grilla de entradas según dimensiones
    def generate_matrix():
        nonlocal current_rows, current_cols
        error_label.configure(text="")
        result_label.configure(text="")
        for widget in matrix_frame.winfo_children():
            widget.destroy()
        entries.clear()
        calculate_btn.configure(state="disabled")
        try:
            rows = int(rows_entry.get())
            cols = int(cols_entry.get())

            # Validar que filas y columnas no sean mayores a 4
            if rows > 4 or cols > 4:
                raise ValueError("Las matrices no pueden ser mayores a 4x4.")

            build_matrix_from_input(rows, cols, [0]*(rows*cols))

            current_rows, current_cols = rows, cols
            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    e = ctk.CTkEntry(matrix_frame, width=50)
                    e.grid(row=i, column=j, padx=5, pady=5)
                    row_entries.append(e)
                entries.append(row_entries)

            calculate_btn.configure(state="normal")
        except ValueError as ve:
            error_label.configure(text=str(ve))

    # Función para calcular inversa usando logic/inversa.py
    def calculate_inverse():
        error_label.configure(text="")
        result_label.configure(text="")
        try:
            values = []
            for row_list in entries:
                for entry in row_list:
                    values.append(float(entry.get()))

            matrix = build_matrix_from_input(current_rows, current_cols, values)
            matrix_list = matrix.tolist()
            inversa = matriz_inversa(matrix_list)

            # Formatear matriz inversa de forma amigable
            result_str = "Matriz inversa:\n\n"
            for row in inversa:
                formatted_row = "   ".join(f"{val:7.2f}" for val in row)
                result_str += formatted_row + "\n"
            result_label.configure(text=result_str)

        except ValueError as ve:
            error_label.configure(text=str(ve))
        except Exception:
            error_label.configure(text="Ingrese todos los valores correctamente.")

    generate_btn.configure(command=generate_matrix)
    calculate_btn.configure(command=calculate_inverse)
