# Programa para mostrar las tablas de multiplicar del 1 al 10

def tablas_de_multiplicar():
    for i in range(1, 11):  # Itera del 1 al 10
        print(f"Tabla del {i}:")
        for j in range(1, 11):  # Multiplica del 1 al 10
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()  # Línea en blanco para separar las tablas

# Llamar a la función
tablas_de_multiplicar()