# modos de lectura de ficheros:
# r: lectura - read = Solo para leer el fichero
# a: anexar - append = escribir al final del fichero
# w: escritura - write = Sobreescribe todo el fichero
# x: crear - create = Crear fichero
# t: texto - text = texto plano
# b: binario - binary = binario
# +: lectura y escritura


# f = open('/Users/leone/documents/prueba.txt', 'r')
# print(f.read())

# f.close


# ______________________________________________

# def main():
#     usuarios = listarUsuarios()
#     for usuarios in usuarios:
#         print(f'usuario: {usuarios} ')


# nombresUsuarios = []


# def listarUsuarios():
#     f = open('/users/leone/documents/prueba.txt', 'r')
#     datos = f.readlines()
#     f.close

#     for linea in datos:
#         if linea[0] == '#':
#             continue

#         if linea[0] == '_' or linea == '\n':
#             continue

#         partes = linea.split(':')
#         nombresUsuarios.append(partes[0])
#     return nombresUsuarios


# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------

# def escribe(fichero, datos):
#     f = open('miFichero.txt', 'w')

#     for linea in datos:
#         if not linea.endswith('\n'):
#             linea += '\n'
#         f.write(linea)

#     f.close()


# lista = [
#     'Esta es una linea 1', 'Esta es la liena 2', 'Esta es la linea 3']

# escribe('miFichero.txt', lista)

# -------------------------------------------------------
# Serializacion de datos: convertir un oibjeto o cualquiier otra cosa, a una secuencia de datos que se pueda escribir en un fichero (algo entendible en un programa como un  objeto).

# from msilib.schema import Class
# import pickle


# class Juguete:
#     nombre = ' '
#     precio = 0.0

#     def __init__(self, nombre, precio) -> None:
#         self.nombre = nombre
#         self.precio = precio

#     def getNombre(self):
#         return self.nombre


# f = open('datos.bin', 'rb')

# pote = pickle.load(f)
# f.close
# print(type(pote))
# print(f'{pote.getNombre()} Tiene un precio de: {pote.precio}')


class Vehiculo:
    _status = False

    def __init__(self):
        self.tipo = 'Coche'

    def encender(self):
        self._status = True
        print(f'El {self.tipo} esta: ENCENDIDO')

    def apagar(self):
        self._status = False
        print(f'El {self.tipo} esta: APAGADO')

    def isEncendido(self):
        return self._status


coche = Vehiculo()

