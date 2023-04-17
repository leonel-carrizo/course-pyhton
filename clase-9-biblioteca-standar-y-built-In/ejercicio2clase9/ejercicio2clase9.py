# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce


lista = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14


def impares(x):
    if x % 2 != 0:
        return x


impar = filter(impares, lista)
impar = list(impar)
print(f'Estos son los numeros impares: {impar} ')


def sumar(a, b):
    return a + b


suma = reduce(sumar, impar)
print(f'Y la sumatoria de esos numeros es: {suma}')
