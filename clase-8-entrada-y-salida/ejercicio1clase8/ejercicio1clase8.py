# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
from os import path


def main():

    f = open('fichero1.txt', 'w')
    f.write('Este es un texto para el fichero.\n')
    f.write('Clase 8: Entrada-Salida\n')

    f.close

    f = open('fichero1.txt', 'r')
    fichero = f.read()

    print(fichero)
    f.close


# Comprobar la carpeta dode se creo el fichero
name_file = 'fichero1.txt'
print(f'El fichero se encuentra en la carpeta: {path.abspath(name_file)}')

if __name__ == '__main__':
    main()
