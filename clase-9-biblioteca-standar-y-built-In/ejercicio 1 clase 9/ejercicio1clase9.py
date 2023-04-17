# Crea un script que le pida al usuario una lista de países(separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos(haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

entrada = input(
    'Introduzaca 5 nombres de Paises separados por  una coma \',\':')

listaA = str.split(entrada)


def quitarComa(x):
    x = str.title(x)
    if str(x).endswith(','):
        x = str(x)[:-1]
        return x
    return x


sinComa = map(quitarComa, listaA)
paises = set(sinComa)

print('Los Paises ingresados son:', sorted(paises))
