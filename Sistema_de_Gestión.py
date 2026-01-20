import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# --- BASE DE DATOS (Actualizada con nuevos campos) ---
def conectar_db():
    conn = sqlite3.connect("gestion_grafica.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            direccion TEXT,
            email TEXT,
            servicio TEXT,
            total REAL,
            pago REAL,
            metodo TEXT,
            estado TEXT
        )
    ''')
    conn.commit()
    return conn

# --- LÓGICA ---
def actualizar_tabla():
    for item in tabla.get_children():
        tabla.delete(item)
    conn = conectar_db()
    cursor = conn.cursor()
    # Traemos los datos para mostrar en la lista
    cursor.execute("SELECT id, cliente, servicio, total, pago, estado, direccion FROM pedidos ORDER BY id DESC")
    for f in cursor.fetchall():
        saldo = f[3] - f[4]
        # Mostramos los datos principales en la tabla
        tabla.insert("", tk.END, values=(f[0], f[1], f[2], f[3], saldo, f[5], f[6]))
    conn.close()

def registrar_pedido():
    if not (ent_nom.get() or ent_dir.get()):
        messagebox.showwarning("Atención", "Nombre y Dirección son importantes para el envío")
        return
    
    try:
        total = float(ent_tot.get())
        pago = float(ent_pag.get())
        estado = "Entregado" if pago >= total else "Pendiente"
        
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO pedidos (cliente, direccion, email, servicio, total, pago, metodo, estado) 
                          VALUES (?,?,?,?,?,?,?,?)''', 
                       (ent_nom.get(), ent_dir.get(), ent_eml.get(), cmb_ser.get(), total, pago, cmb_met.get(), estado))
        conn.commit()
        conn.close()
        actualizar_tabla()
        limpiar()
        messagebox.showinfo("Guardado", "Pedido registrado con éxito")
    except ValueError:
        messagebox.showerror("Error", "En Total y Seña solo debes poner números")

def marcar_entregado():
    item_sel = tabla.selection()
    if not item_sel: 
        messagebox.showwarning("Atención", "Selecciona un pedido de la lista")
        return
    id_p = tabla.item(item_sel)['values'][0]
    total_p = tabla.item(item_sel)['values'][3]
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE pedidos SET estado='Entregado', pago=? WHERE id=?", (total_p, id_p))
    conn.commit()
    conn.close()
    actualizar_tabla()

def limpiar():
    ent_nom.delete(0, tk.END); ent_dir.delete(0, tk.END)
    ent_eml.delete(0, tk.END); ent_tot.delete(0, tk.END); ent_pag.delete(0, tk.END)

# --- INTERFAZ ---
root = tk.Tk()
root.title("Gestión de Gráfica y Logística - Control de Entregas")
root.geometry("1100x650")

# Formulario Expandido
f_arr = tk.LabelFrame(root, text=" Datos del Pedido y Entrega ", padx=15, pady=15)
f_arr.pack(fill="x", padx=20, pady=10)

# Fila 1: Datos Personales
tk.Label(f_arr, text="Nombre Cliente:").grid(row=0, column=0, sticky="e")
ent_nom = tk.Entry(f_arr, width=30)
ent_nom.grid(row=0, column=1, padx=5, pady=5)

tk.Label(f_arr, text="Dirección (B°, Calle, N°):").grid(row=0, column=2, sticky="e")
ent_dir = tk.Entry(f_arr, width=40)
ent_dir.grid(row=0, column=3, padx=5, pady=5)

# Fila 2: Contacto y Servicio
tk.Label(f_arr, text="Correo Electrónico:").grid(row=1, column=0, sticky="e")
ent_eml = tk.Entry(f_arr, width=30)
ent_eml.grid(row=1, column=1, padx=5, pady=5)

tk.Label(f_arr, text="Tipo de Trabajo:").grid(row=1, column=2, sticky="e")
cmb_ser = ttk.Combobox(f_arr, values=["Sublimación", "Ploteo", "Impresión 3D", "Fotografía", "Textil a Medida"], width=37)
cmb_ser.current(0); cmb_ser.grid(row=1, column=3, padx=5, pady=5)

# Fila 3: Dinero
tk.Label(f_arr, text="Total $:").grid(row=2, column=0, sticky="e")
ent_tot = tk.Entry(f_arr, width=15)
ent_tot.grid(row=2, column=1, padx=5, pady=5, sticky="w")

tk.Label(f_arr, text="Seña $:").grid(row=2, column=2, sticky="e")
ent_pag = tk.Entry(f_arr, width=15)
ent_pag.grid(row=2, column=3, padx=5, pady=5, sticky="w")

tk.Label(f_arr, text="Pago:").grid(row=2, column=3, sticky="e")
cmb_met = ttk.Combobox(f_arr, values=["Efectivo", "Transferencia", "Mercado Pago / QR"], width=15)
cmb_met.current(0); cmb_met.grid(row=2, column=4, padx=5, pady=5)

tk.Button(f_arr, text="GUARDAR PEDIDO", bg="#28a745", fg="white", font=("Arial", 10, "bold"), command=registrar_pedido, width=20).grid(row=0, column=5, rowspan=3, padx=20)

# Tabla de Gestión
f_aba = tk.LabelFrame(root, text=" Pedidos Activos y Hoja de Ruta ")
f_aba.pack(fill="both", expand=True, padx=20, pady=10)

cols = ("ID", "Cliente", "Trabajo", "Total $", "Saldo Pend.", "Estado", "Dirección de Entrega")
tabla = ttk.Treeview(f_aba, columns=cols, show="headings")
for c in cols: 
    tabla.heading(c, text=c)
    if c == "Dirección de Entrega":
        tabla.column(c, width=250) # Más ancho para leer bien la dirección
    else:
        tabla.column(c, width=100)
tabla.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(root, text="MARCAR COMO ENTREGADO (PAGO TOTAL RECIBIDO)", bg="#007bff", fg="white", font=("Arial", 11, "bold"), command=marcar_entregado, pady=12).pack(pady=15)

conectar_db()
actualizar_tabla()
root.mainloop()