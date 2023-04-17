# temperatura = 12.0

# def miFunsion(nombre = 'leonel'):
#     print("hola, ", nombre)


# def suma(a=1, b=5, c=1):
#     print(a + b + c)

# suma(c = 9)

# def suma1(**kwargs):
#     print(kwargs)


# suma1(1,1)

from ast import Or
from ctypes.wintypes import PINT
from unittest import result


def saludar ():
    print('hola que tal')
    print(' ')

# saludar()
# saludar()

#funsiones con argumentos

def saludar2(nombre):
    print('hola ' + nombre + ' Que tal?')

# saludar2('Leonel')
# saludar2('Remi')

# Finsiones con retorno

def suma(a, b):
    resultado = a + b
    return resultado
    print(' ')


# valor = suma(10, 5)
# print(valor)
# valor = suma(23, 12)
# print(valor)

def suma2(a, b):
    return a + b

# valor = suma2(10, 5)
# print(valor)

def sonIguales(num1, num2):
    return num1 == num2

# verdad = sonIguales(3, 3)
# if (verdad):
#     print('Son iguales!!!')
# else:
#     print('No son iguales')
# print(verdad)

# verdad = sonIguales(3,5)
# print(verdad)

# Funsiones con argumentos con valor por defecto

def saludaPorDefectro(nombre='Dimas'):
    print('Hola ' +  nombre + ' ¿Qué tal?')

# saludaPorDefectro()
# saludaPorDefectro('Remi')

# funsiones que retornan varios valores

def sumYRestas(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

# resultado1, resultado2 = sumYRestas(10, 15)
# print('Los resultados son:\nSuma: '+ str(resultado1) + '\nResta: ' + str(resultado2))

num1 = input('ingrese un numero: ')
num2 = input('Ingrese otro numero:')

def maximo(a, b):
    if ((type(a) == float or type(a) == int) and (type(b) == float or type(b) == int )):
        if a == b:
            print('Los numero son iguales'+'\n')
        elif a > b:
            return a
        else:
            return b
    else:
        return False

valorMaximo = maximo(num1, num2)
if valorMaximo == False:
        print('ERROR!! solo se admiten numeros')
if valorMaximo:
    print('El valor MAXIMO es: ' + str(valorMaximo)+'\n')