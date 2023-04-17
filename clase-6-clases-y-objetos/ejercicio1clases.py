# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color, Ruedas, Puertas,

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad, Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = 'Negro'
    ruedas = 4
    puertas = 5


class Coche:
    velocidad = 120
    cilindrada = 4

    def showVelocidad(self):
        return self.velocidad

    def showCilindrada(self):
        return self.cilindrada


c = Coche()
print('El coche es de :', c.showCilindrada(), 'cilindros',
      'y su velocidad es de: ', c.showVelocidad())
