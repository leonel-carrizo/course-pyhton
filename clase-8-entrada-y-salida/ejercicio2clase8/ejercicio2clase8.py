# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
from email.mime import audio
import pickle


class Vehiculo:
    _status = None

    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        self._status = True

    def apagar(self):
        self._status = False

    def isEncendido(self):
        if self._status:
            return (f'El {self.tipo} está ENCENDIDO')
        else:
            return (f'El {self.tipo} está APAGADO')


auto = Vehiculo('Camion')
f = open('claseVehiculo.py',  'wb')
pickle.dump(auto, f)
f.close


f = open('claseVehiculo.py', 'rb')
claseVehiuclo = pickle.load(f)
f.close()

auto.encender()
print(auto.isEncendido())

auto.apagar()
print(auto.isEncendido())
