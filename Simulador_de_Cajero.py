import tkinter as tk
from tkinter import messagebox, simpledialog

# -------------------------
# Variables globales
# -------------------------
productos = []
cantidad_esperada = 0

# -------------------------
# Funciones
# -------------------------
def iniciar_compra():
    global cantidad_esperada

    productos.clear()
    entrada.delete(0, tk.END)

    try:
        cantidad = simpledialog.askinteger(
            "Cantidad de productos",
            "¿Cuántos productos desea ingresar?"
        )

        if cantidad is None or cantidad <= 0:
            messagebox.showwarning(
                "Atención",
                "Debe ingresar un número mayor a 0."
            )
            return

        cantidad_esperada = cantidad
        etiqueta.config(
            text=f"Ingrese el monto del producto 1 de {cantidad_esperada}:"
        )

    except Exception:
        messagebox.showerror("Error", "Entrada no válida.")


def agregar_monto():
    global cantidad_esperada

    try:
        monto = float(entrada.get())
        productos.append(monto)
        entrada.delete(0, tk.END)

        if len(productos) < cantidad_esperada:
            etiqueta.config(
                text=f"Ingrese el monto del producto {len(productos) + 1} de {cantidad_esperada}:"
            )
        else:
            mostrar_resultado()

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")


def mostrar_resultado():
    total = sum(productos)
    cantidad = len(productos)

    resumen = f"Cantidad de productos: {cantidad}\n"
    resumen += f"Total a pagar: ${total:.2f}\n\n"
    resumen += "Montos individuales:\n"

    for i, monto in enumerate(productos, start=1):
        resumen += f" Producto {i}: ${monto:.2f}\n"

    messagebox.showinfo("Resumen de compra", resumen)

    # Limpiamos todo después del ticket
    reiniciar()


def reiniciar():
    global productos, cantidad_esperada

    productos = []
    cantidad_esperada = 0

    entrada.delete(0, tk.END)
    etiqueta.config(text="Hacé clic en 'Iniciar compra' para empezar")

    messagebox.showinfo(
        "Reiniciado",
        "Todos los datos fueron reiniciados."
    )

# -------------------------
# Crear ventana
# -------------------------
ventana = tk.Tk()
ventana.title("Simulación de Caja")

etiqueta = tk.Label(
    ventana,
    text="Hacé clic en 'Iniciar compra' para empezar"
)
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_iniciar = tk.Button(
    frame_botones,
    text="Iniciar compra",
    command=iniciar_compra,
    width=12
)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_agregar = tk.Button(
    frame_botones,
    text="Agregar monto",
    command=agregar_monto,
    width=12
)
boton_agregar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(
    frame_botones,
    text="Reiniciar",
    command=reiniciar,
    width=12
)
boton_reiniciar.grid(row=0, column=2, padx=5)

ventana.mainloop()