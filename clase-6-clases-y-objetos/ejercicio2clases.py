# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno:
    _aprobado = False

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprueba(self):
        self._aprobado = True

    def reprueba(self):
        self._aprobado = False


alumno = Alumno('Carlos Ramirez', 70)
# Si la nota del alumno es menor a 70 puntos estará reprobado
if alumno.nota >= 70:
    alumno.aprueba()
    a = 'APROBADO'

else:
    alumno.reprueba()
    a = 'Reprobado'

print('Nombre:', alumno.nombre + '. ', 'Nota: ',
      alumno.nota, '. ', 'Se encuentra: ', a)
