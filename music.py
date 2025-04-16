import music21  # Librería para trabajar con música

class Partitura:
    def __init__(self, título, compás, tempo):
        self.título = título
        self.compás = compás
        self.tempo = tempo
        self.notas = []

    def agregar_nota(self, nota, duración):
        self.notas.append((nota, duración))

    def mostrar_partitura(self):
        stream = music21.stream.Stream()
        stream.append(music21.metadata.Metadata(title=self.título))
        stream.append(music21.tempo.MetronomeMark(number=self.tempo))
        stream.append(music21.meter.TimeSignature(self.compás))

        for nota, duración in self.notas:
            stream.append(music21.note.Note(nota, quarterLength=duración))

        stream.show('musicxml')

def main():
    título = input("Ingrese el título de la partitura: ")
    compás = input("Ingrese el compás (e.g. 4/4): ")
    tempo = int(input("Ingrese el tempo (e.g. 120): "))

    partitura = Partitura(título, compás, tempo)

    while True:
        nota = input("Ingrese una nota (e.g. C4): ")
        duración = float(input("Ingrese la duración de la nota (e.g. 1.0): "))
        partitura.agregar_nota(nota, duración)

        respuesta = input("¿Desea agregar otra nota? (s/n): ")
        if respuesta.lower() != 's':
            break

    partitura.mostrar_partitura()

if __name__ == "__main__":
    main()