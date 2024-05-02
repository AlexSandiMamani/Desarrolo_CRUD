import sqlite3
from datetime import datetime

# Nombre del archivo de la base de datos
DB_FILE = 'alumnos.db'

# Conexión a la base de datos
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                    codigo INTEGER PRIMARY KEY,
                    apellido_paterno TEXT,
                    apellido_materno TEXT,
                    nombres TEXT,
                    carrera_profesional TEXT,
                    domicilio TEXT,
                    fecha_nacimiento DATE
                )''')
conn.commit()

# Funciones CRUD
def crear_alumno(codigo, apellido_paterno, apellido_materno, nombres, carrera_profesional, domicilio, fecha_nacimiento):
    cursor.execute('''INSERT INTO alumnos (codigo, apellido_paterno, apellido_materno, nombres, carrera_profesional, domicilio, fecha_nacimiento)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (codigo, apellido_paterno, apellido_materno, nombres, carrera_profesional, domicilio, fecha_nacimiento))
    conn.commit()
    print("Alumno creado correctamente.")

def leer_alumnos():
    cursor.execute('''SELECT * FROM alumnos''')
    alumnos = cursor.fetchall()
    for alumno in alumnos:
        print(alumno)

def actualizar_alumno(codigo, **kwargs):
    update_query = '''UPDATE alumnos SET {} WHERE codigo = ?'''.format(', '.join([f'{key} = ?' for key in kwargs.keys()]))
    cursor.execute(update_query, tuple(kwargs.values()) + (codigo,))
    conn.commit()
    print("Alumno actualizado correctamente.")

def eliminar_alumno(codigo):
    cursor.execute('''DELETE FROM alumnos WHERE codigo = ?''', (codigo,))
    conn.commit()
    print("Alumno eliminado correctamente.")

# Función para mostrar el menú y procesar la opción seleccionada
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Crear alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")
    return opcion

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            # Crear un nuevo alumno
            codigo = int(input("Ingrese el código del alumno: "))
            apellido_paterno = input("Ingrese el apellido paterno del alumno: ")
            apellido_materno = input("Ingrese el apellido materno del alumno: ")
            nombres = input("Ingrese los nombres del alumno: ")
            carrera_profesional = input("Ingrese la carrera profesional del alumno: ")
            domicilio = input("Ingrese el domicilio del alumno: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")

            crear_alumno(codigo, apellido_paterno, apellido_materno, nombres, carrera_profesional, domicilio, fecha_nacimiento)
        elif opcion == "2":
            # Mostrar todos los alumnos
            print("Todos los alumnos:")
            leer_alumnos()
        elif opcion == "3":
            # Actualizar un alumno
            codigo = int(input("Ingrese el código del alumno a actualizar: "))
            nombres = input("Ingrese los nuevos nombres del alumno: ")
            domicilio = input("Ingrese el nuevo domicilio del alumno: ")

            actualizar_alumno(codigo, nombres=nombres, domicilio=domicilio)
        elif opcion == "4":
            # Eliminar un alumno
            codigo = int(input("Ingrese el código del alumno a eliminar: "))
            eliminar_alumno(codigo)
        elif opcion == "5":
            # Salir del programa
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Cerrar la conexión a la base de datos al finalizar
conn.close()
