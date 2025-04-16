import keyboard

# Tu código existente aquí

# Definir la función que se ejecutará cuando se presione la tecla escape

def convertir_a_binario(nombre):
    # Convierte cada letra del nombre a su representación binaria
    # utilizando la función ord() que devuelve el valor ASCII de un carácter.
    # Luego, utiliza la función bin() para obtener la representación binaria.
    # Finalmente, une todos los resultados en una cadena.
    nombre_binario = ''.join(bin(ord(letra))[2:] for letra in nombre)

    return nombre_binario

def on_escape_key(event):
    if event.name == 'esc':
        keyboard.unhook_all()  # Detiene la detección de teclas
        print("Se ha presionado la tecla de escape. El bucle ha terminado.")

# Agregar el gancho (hook) para detectar la pulsación de teclas
keyboard.on_press(on_escape_key)

# Bucle "for" que se ejecutará hasta que se presione la tecla de escape
for i in range():
    print("Iteración:", i)
    # Tu código dentro del bucle "for" aquí

# Solicita al usuario que ingrese un nombre
nombre = input("Ingrese un nombre: ")

# Llama a la función convertir_a_binario() y muestra el resultado
resultado = convertir_a_binario(nombre)
print(f"El nombre {nombre} en binario es: {resultado}")

# Mantener el programa en ejecución hasta que se presione la tecla de escape
keyboard.wait('Esc')