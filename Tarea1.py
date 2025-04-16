from Word import mostrar_tablero, obtener_palabra_aleatoria


print("Hello World!")
secret_number= 20


def juego_adivina_palabra():
    palabra = obtener_palabra_aleatoria()
    palabra_oculta = ["_" for _ in palabra];
    intentos = 3
    letras_usadas = []

    while true:
       mostrar_tablero(palabra_oculta,intentos)

       if "_" not in palabra_oculta:
           print("¡Ganaste! La palabra es:", " ".join(palabra))
           break
       if intentos == 0:
           print("¡LOSER! La palabra es:", " ".join(palabra))
           break


       letra = imput("ingresa una letra ").lower()

       if letra in letras_adivinadas:
            print("ya adivinaste esta letra, intenta con otra")
            continue
    letras_usadas.append(letras)

    aciertos = adivinar_letras(palabra,palabra_oculta,letra)

    if aciertos > 0:
        print("¡Adivinaste!", aciertos, "letras")
    else:
        print("Esa letra no se encuentra en la palabra oculta")
        intentos -= 1
        print("===========================")


    juego_adivina_palabra()