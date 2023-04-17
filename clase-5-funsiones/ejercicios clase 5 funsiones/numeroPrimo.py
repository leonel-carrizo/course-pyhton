# Escribe una función que pueda decirte si un número (número entero) es primo o no.

numero = 3473

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

comprobador = primo(numero)
if comprobador == False:
    print('El numero ' + str(numero) + ' NO ES Primo'+'\n')
else:
    print('El numero ' + str(numero) + ' ES PRIMO'+'\n')
