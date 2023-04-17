# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


def main():

    def escribeFichero(fichero, datos):
        f = open('archivo1.txt', 'w')

        for linea in datos:
            if linea[-1] != '\n':
                linea += '\n'
            f.write(linea)

        f.close

    lista = [
        'Esta es la linea 1 del fichero',
        'Esta es la linea 2 del fichero',
        'Esta es la linea 3 del fichero',
        'Esta es la linea 4 del fichero',
        'Esta es la linea 5 del fichero.'
    ]

    escribeFichero('archivo1.txt', lista)


if __name__ == '__main__':
    main()
