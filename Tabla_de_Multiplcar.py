import random

# Función para mostrar la tabla de multiplicar de un número
def mostrar_tabla_de_multiplicar(número):
    for i in range(1, 11):
        print(f"{número} x {i} = {número * i}")

# Pedir al usuario que ingrese el número de la tabla
número = int(input("¿Qué tabla de multiplicar deseas ver? Ingresa un número: "))

# Mostrar la tabla de multiplicar del número ingresado
print(f"\nTabla de multiplicar del {número}:\n")
mostrar_tabla_de_multiplicar(número)