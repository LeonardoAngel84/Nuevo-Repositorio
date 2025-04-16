import random

def generar_lista_aleatoria(tamaño):
    lista = []
    for _ in range(tamaño):
        lista.append(random.randint(1, 1000))  # Genera números aleatorios entre 1 y 1000
    return lista

def ordenar_lista(lista):
    return sorted(lista)  # Ordena la lista de menor a mayor

def main():
    tamaño = 100
    lista_aleatoria = generar_lista_aleatoria(tamaño)
    lista_ordenada = ordenar_lista(lista_aleatoria)
    
    print("Lista aleatoria:")
    print(lista_aleatoria)
    print("\nLista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()