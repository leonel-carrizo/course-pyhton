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

    # Funsion crea base de datos
    def creaBD():
        conn = sql.connect('miaplicacion.db')
        conn.commit()
        conn.close()

    # Funsion crea Tabla
    def creatabla():
        conn = sql.connect('miaplicacion.db')
        curor = conn.cursor()
        curor.execute(
            '''CREATE TABLE Alumnos(id INTEGER PRIMARY KEY, Nombres TEXT, Apellidos TEXT)'''
        )
        conn.commit()
        conn.close()

    # Funsion que agraga una ListaAlumnos a la BD
    def insertLista(Alumnos):
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        rows = f"INSERT INTO Alumnos VALUES (?, ?, ?)"
        cursor.executemany(rows, Alumnos)
        conn.commit()
        conn.close()

    # Funsion que agraga una Row a la BD
    def insertRow(id, nombre, apellido):
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        rows = f"INSERT INTO Alumnos VALUES ({id}, '{nombre}', '{apellido}') "
        cursor.execute(rows)
        conn.commit()
        conn.close()

    # Funsion para borrar Toda
    def borrarBD(id):
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Alumnos WHERE{id}")
        cursor.fetchall()
        conn.commit()
        conn.close()

    # Funsion para borrar una Fila
    def deleteRow(id):
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Alumnos WHERE id = {id}")
        cursor.fetchall()
        conn.commit()
        conn.close()

    # Finsion para leer datos de la Tabla por ID
    def leeRows():
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Alumnos ")
        datos = cursor.fetchall()
        print(datos)
        conn.close()

    # Funsion leer los datos de una fila por Nombre
    def leerAlumno(nombre):
        conn = sql.connect('miaplicacion.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Alumnos WHERE Nombres = ('{nombre}') ")
        datos = cursor.fetchall()
        print(datos)
        conn.close()

    # creaBD()
    # creatabla()
    # insertLista()
    # insertRow(1, 'Luz', 'Maribel')
    # borrarBD(10)
    # deleteRow(1)
    leerAlumno('Marcelo')
    # leeRows()


if __name__ == '__main__':
    main()
