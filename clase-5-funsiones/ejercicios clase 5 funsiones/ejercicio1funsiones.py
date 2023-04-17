# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.


from math import pi

# Calculo del área de un triangulo Isóceles
def areaTriangulo(base, altura):
    return (1/2)*base*altura

resultado = areaTriangulo(4, 5)
print('El area del triangulo es: ' + str(resultado) + '\n')

# Calculo del área del Circulo
def areaCirculo(radio):
    return round (pi*radio**2,4)

area2 = areaCirculo(12)
print('El área del circulo es: ' + str(area2) + '\n')