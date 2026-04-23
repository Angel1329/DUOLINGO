import customtkinter as ctk

class AppDuolingo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PyLingo - Aprende Inglés")
        self.geometry("400x500")
        ctk.set_appearance_mode("light") # Modo claro/oscuro

        # Datos de ejemplo
        self.lecciones = [
            {"pregunta": "The bread", "respuesta": "El pan"},
            {"pregunta": "The milk", "respuesta": "La leche"},
            {"pregunta": "I eat", "respuesta": "Yo como"},
            {"pregunta": "Like", "respuesta": "Me gusta"}
        ]
        self.indice = 0
        self.puntos = 0

        # --- Elementos de la Interfaz ---
        
        # 1. Barra de Progreso
        self.barra_progreso = ctk.CTkProgressBar(self, width=300)
        self.barra_progreso.set(0)
        self.barra_progreso.pack(pady=30)

        # 2. Etiqueta de la Pregunta
        self.label_instruccion = ctk.CTkLabel(self, text="Traduce esta frase:", font=("Arial", 14))
        self.label_instruccion.pack(pady=10)

        self.label_pregunta = ctk.CTkLabel(self, text=self.lecciones[0]["pregunta"], font=("Arial", 24, "bold"))
        self.label_pregunta.pack(pady=20)

        # 3. Entrada de texto
        self.entrada = ctk.CTkEntry(self, placeholder_text="Escribe en español...", width=250, height=40)
        self.entrada.pack(pady=20)

        # 4. Botón de Comprobar
        self.boton_comprobar = ctk.CTkButton(self, text="COMPROBAR", fg_color="#58cc02", hover_color="#46a302", 
                                            text_color="white", font=("Arial", 14, "bold"), command=self.verificar_respuesta)
        self.boton_comprobar.pack(pady=20)

        # 5. Feedback (Correcto/Incorrecto)
        self.label_feedback = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.label_feedback.pack(pady=10)

    def verificar_respuesta(self):
        respuesta_usuario = self.entrada.get().strip().lower()
        respuesta_correcta = self.lecciones[self.indice]["respuesta"].lower()

        if respuesta_usuario == respuesta_correcta:
            self.label_feedback.configure(text="¡Excelente! ✨", text_color="green")
            self.puntos += 1
        else:
            self.label_feedback.configure(text=f"Incorrecto. Era: {respuesta_correcta}", text_color="red")

        # Avanzar a la siguiente pregunta
        self.indice += 1
        progreso = self.indice / len(self.lecciones)
        self.barra_progreso.set(progreso)

        if self.indice < len(self.lecciones):
            # Limpiar entrada y cambiar pregunta
            self.entrada.delete(0, 'end')
            self.label_pregunta.configure(text=self.lecciones[self.indice]["pregunta"])
        else:
            self.finalizar()

    def finalizar(self):
        self.label_pregunta.configure(text="¡Lección Terminada!")
        self.entrada.destroy()
        self.boton_comprobar.destroy()
        self.label_feedback.configure(text=f"Puntaje: {self.puntos}/{len(self.lecciones)}")

if __name__ == "__main__":
    app = AppDuolingo()
    app.mainloop()


