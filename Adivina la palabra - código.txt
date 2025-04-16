import tkinter as tk
import random

class JuegoAdivinaPalabra:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinar Palabra")

        self.palabra = self.obtener_palabra_aleatoria()
        self.palabra_oculta = ["_" for _ in self.palabra]
        self.intentos_restantes = 5
        self.letras_usadas = []

        self.palabra_label = tk.Label(root, text="Palabra oculta: " + " ".join(self.palabra_oculta), font=('Arial', 16))
        self.palabra_label.pack(pady=10)

        self.intentos_label = tk.Label(root, text="Intentos restantes: " + str(self.intentos_restantes), font=('Arial', 14))
        self.intentos_label.pack()

        self.letra_label = tk.Label(root, text="Ingresa una letra:", font=('Arial', 14))
        self.letra_label.pack(pady=5)

        self.letra_var = tk.StringVar()
        self.letra_entry = tk.Entry(root, textvariable=self.letra_var, font=('Arial', 14))
        self.letra_entry.pack()

        self.adivinar_button = tk.Button(root, text="Adivinar", font=('Arial', 14), command=self.adivinar_letra)
        self.adivinar_button.pack(pady=5)

        self.resultado_label = tk.Label(root, text="", font=('Arial', 14))
        self.resultado_label.pack(pady=10)

    def obtener_palabra_aleatoria(self):
        palabras = ("Agustin", "Tobias", "Luana", "Martina", "Sofia", "Isabela", "Miguelito", "Clarisa", "Leonardo",
                    "Nicolás", "Pablo", "Guillermo", "Papi Pelusa", "Mami Ester")
        return random.choice(palabras)

    def adivinar_letra(self):
        letra = self.letra_var.get().lower()

        if letra in self.letras_usadas:
            self.resultado_label.config(text="Ya adivinaste esta letra, intenta con otra.")
            return

        self.letras_usadas.append(letra)

        aciertos = 0
        for i in range(len(self.palabra)):
            if self.palabra[i].lower() == letra:
                self.palabra_oculta[i] = self.palabra[i]
                aciertos += 1

        if aciertos > 0:
            self.resultado_label.config(text=f"¡Adivinaste {aciertos} letras!")
        else:
            self.resultado_label.config(text="Esa letra no se encuentra en la palabra oculta")
            self.intentos_restantes -= 1
            self.intentos_label.config(text="Intentos restantes: " + str(self.intentos_restantes))

        if "_" not in self.palabra_oculta:
            self.resultado_label.config(text=f"¡Ganaste! La palabra es: {' '.join(self.palabra)}")
            self.adivinar_button.config(state='disabled')
        elif self.intentos_restantes == 0:
            self.resultado_label.config(text=f"¡LOSER! La palabra era: {' '.join(self.palabra)}")
            self.adivinar_button.config(state='disabled')

        self.palabra_label.config(text="Palabra oculta: " + " ".join(self.palabra_oculta))
        self.letra_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinaPalabra(root)
    root.mainloop()