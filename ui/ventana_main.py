import customtkinter as ctk
from ui.apartado_inversa import setup_inverse_tab

def run_app():
    # Configuración básica de apariencia
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Ventana principal
    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Calculadora de Matrices")

    # Contenedor de pestañas
    tabview = ctk.CTkTabview(app)
    tabview.pack(fill="both", expand=True, padx=20, pady=20)

    # Definir pestañas vacías
    tabview.add("Suma")
    tabview.add("Resta")
    tabview.add("Multiplicación")
    tabview.add("Inversa")
    tabview.add("Determinante")

    # Llamamos a la función que configura la pestaña de Inversa
    setup_inverse_tab(tabview.tab("Inversa"))

    app.mainloop()
