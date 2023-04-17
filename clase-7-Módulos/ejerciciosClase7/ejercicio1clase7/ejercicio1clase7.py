# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.  Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

from moduloMath import sumar, restar, multiplicador, dividir


def main():

    miSuma = sumar(2, 2)
    print(miSuma)

    miResta = restar(2, 2)
    print(miResta)

    miMulti = multiplicador(2, 2)
    print(miMulti)

    miDiv = dividir(2, 2)
    print(miDiv)


if __name__ == '__main__':
    main()
