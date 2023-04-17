# Clases dinamicas
from abc import ABC, abstractclassmethod, abstractmethod


class Dino:
    _encendido = True

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


d = Dino()
d.apaga()
# print(d._encendido)

# Clases Estaticas


class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1


# Estatica.incrementa()
# print(Estatica.numero)
# Estatica.incrementa()
# print(Estatica.numero)
# Estatica.incrementa()
# print(Esatica.numero)

# Herencia


class Juguete():
    _encendido = True

    # def __init__(self):
    #print('Estoy en el contructor del padre juguete')

    def enciende(self):
        print('Enciendo el aparato')
        self._encendido = True

    def apaga(self):
        print('apago el aparato')
        self._encendido = False

    def isEncendido(self):
        return self._encendido


class Potato(Juguete):
    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass


class Dino(Potato, Juguete):
    def verEscamas(sefl):
        pass


p = Dino()


# constructores:

class Dino(Juguete):
    color = None

    def __init__(self, nombre):
        super().__init__()
        #print('Estoy en el constructor de la clase Dino')


# clases abstractas:


class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def diHola(self):
        print('Hola')


class Perro(Animal):
    def sonido(self):
        print('Guau')


class Gato(Animal):
    def sonido(self):
        print('Miau')


# p = Perro()
# p.sonido()
# p.diHola()

# g = Gato()
# g.sonido()
# p.diHola()


# Relaciones HAS-A

    # composición: Una clase esta compuesta de otrtas clases.


class Motor:
    tipo = 'Diesel'


class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor


class Ruedas:
    cantidad = 4


class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()


class Coche:
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print('El Motor es ', c.motor.tipo)
print('Ventanas = ', c.carroceria.ventanas.cantidad)

c.carroceria.ventanas.cambiarCantidad(3)
print('Ventanas = ', c.carroceria.ventanas.cantidad)
