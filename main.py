import customtkinter
from tkinter import messagebox


preguntas = [
    {
        "pregunta": "En que año se fundo el club Newell's Old Boys?",
        "opciones": ["1912", "1905", "1903", "1902"],
        "respuesta_correcta": "1903"
    },
    {
        "pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "opciones": ["Gabriel García Márquez", "Pablo Neruda", "Jorge Luis Borges", "Octavio Paz"],
        "respuesta_correcta": "Gabriel García Márquez"
    },
    {
        "pregunta": "¿Qué país ganó la Copa Mundial de la FIFA en 2022?",
        "opciones": ["Brasil", "Alemania", "Argentina", "Francia"],
        "respuesta_correcta": "Argentina"
    },
    {
        "pregunta": "¿De qué ciudad provienen los Beatles?",
        "opciones": ["Londres", "Liverpool", "Cambridge", "Mánchester"],
        "respuesta_correcta": "Físico teórico"
    }
]


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

ventana = customtkinter.CTk()
ventana.geometry("450x300")
ventana.title("Quiz App")


frame_1 = customtkinter.CTkFrame(master=ventana)
frame_1.pack(pady=20, padx=40, fill="both", expand=True)

pregunta_label = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="")
pregunta_label.pack(pady=10, padx=10)

opcion1 = customtkinter.CTkButton(master=frame_1, text="")
opcion1.pack(pady=10, padx=10)

opcion2 = customtkinter.CTkButton(master=frame_1, text="")
opcion2.pack(pady=10, padx=10)

opcion3 = customtkinter.CTkButton(master=frame_1, text="")
opcion3.pack(pady=10, padx=10)

opcion4 = customtkinter.CTkButton(master=frame_1, text="")
opcion4.pack(pady=10, padx=10)


respuesta_actual = 0
num_errores = 0

def mostrar_pregunta(num_pregunta):
    global respuesta_actual

    pregunta = preguntas[num_pregunta]['pregunta']
    opciones = preguntas[num_pregunta]['opciones']

    pregunta_label.configure(text=pregunta)
    opcion1.configure(text=opciones[0], command=lambda: verificar_respuesta(opciones[0]))
    opcion2.configure(text=opciones[1], command=lambda: verificar_respuesta(opciones[1]))
    opcion3.configure(text=opciones[2], command=lambda: verificar_respuesta(opciones[2]))
    opcion4.configure(text=opciones[3], command=lambda: verificar_respuesta(opciones[3]))

def verificar_respuesta(respuesta):
    global respuesta_actual
    global num_errores

    if respuesta == preguntas[respuesta_actual]['respuesta_correcta']:
        messagebox.showinfo("Respuesta correcta", "¡Bien hecho! La respuesta es correcta.")
        siguiente_button.pack()
    else:
        num_errores += 1
        if num_errores == 2:
            messagebox.showinfo("Límite de errores", "Lo siento, ya has superado el límite de errores para esta pregunta.")
            ventana.destroy()
        else:
            messagebox.showwarning("Respuesta incorrecta", f"Lo siento, la respuesta es incorrecta. Te quedan {2-num_errores} oportunidades para responder correctamente.")

def siguiente_pregunta():

    global respuesta_actual
    global num_errores

    num_errores = 0
    
    if respuesta_actual < len(preguntas) - 1:
        respuesta_actual += 1
        mostrar_pregunta(respuesta_actual)
        siguiente_button.pack_forget()
    else:
        messagebox.showinfo("Fin", "¡Has completado el quiz!")
        ventana.destroy()


siguiente_button = customtkinter.CTkButton(master=ventana, text="Siguiente", command=siguiente_pregunta)

mostrar_pregunta(respuesta_actual)

ventana.mainloop()
