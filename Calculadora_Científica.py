import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        self.display = tk.Entry(root, font=('Arial', 20), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("^", 5, 2), ("C", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("π", 6, 3),
            ("log", 7, 0), ("sqrt", 7, 1), ("exp", 7, 2), ("abs", 7, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, font=('Arial', 15), padx=20, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "π":
            self.display.insert(tk.END, str(math.pi))
        elif text == "sqrt":
            expression = self.display.get()
            result = math.sqrt(eval(expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        else:
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()