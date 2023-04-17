import sqlite3 as sql

def main():
    Alumnos = [
        (1, 'Carmen', 'Castro'),
        (2, 'Pedro', 'Pernia'),
        (3, 'Ricardo', 'Peña'),
        (4, 'Jairo', 'Rondon'),
        (5, 'Marcelo', 'Molina'),
        (6, 'Jorge', 'Acuna'),
        (7, 'Anita', 'Olivar'),
        (8, 'Elba', 'Robersi'),
        (9, 'Jaime', 'Castro'),
        (10, 'Jorge', 'Martinez')
    ]

    def createBD():
        conn = sql.connect('Escuela.db')
        conn.commit()
        conn.close()

    # Funsion crea Tabla
    def createabla():
        conn = sql.connect('Escuela.db')
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE Alumnos(id INTEGER PRIMARY KEY NOT NULL, Nombres TEXT, Apellidos TEXT)'''
        )
        conn.commit()
        cursor.close()
        conn.close()

    # Funsion que agraga una ListaAlumnos a la BD
    def insertLista(Alumnos):
        conn = sql.connect('Escuela.db')
        cursor = conn.cursor()
        rows = f"INSERT INTO Alumnos VALUES (?, ?, ?)"
        cursor.executemany(rows, Alumnos)
        conn.commit()
        cursor.close()
        conn.close()

    # Funsion leer los datos de una fila por Nombre
    def readAlumno(nombre):
        conn = sql.connect('Escuela.db')
        cursor = conn.cursor()
        rows = cursor.execute(
            f"SELECT * FROM Alumnos WHERE Nombres = ('{nombre}') ")
        datos = cursor.fetchone()
        cursor.close()
        conn.close()
        if datos == None:
            print(
                'El nombre no esta en la lista, pruebe poner la primer letra en mayuscula')

        else:
            datos = list(datos)
            print(
                f'ID del Alumno: {datos[0]}, Su Nombre es: {datos[1]} y Apellido: {datos[2]}')

    # tabla =createabla()
    # insertLista(Alumnos)
    readAlumno('Pedro')


if __name__ == '__main__':
    main()
