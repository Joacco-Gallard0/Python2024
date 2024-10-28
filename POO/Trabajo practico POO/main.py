import sqlite3
from ClsEstudiante import Estudiante
from ClsCalificación import Calificacion
from ClsMateria import Materia
from ClsProfesor import Profesor

def conectar_db():
    conn = sqlite3.connect('escuela.db')
    return conn

def main():
    conn = conectar_db()
    cursor = conn.cursor()

    while True:
        print("\nSistema de Gestion Escolar")
        print("1. Agregar estudiante")
        print("2. Agregar profesor")
        print("3. Agregar materia")
        print("4. Agregar calificación")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias")
        print("8. Mostrar calificaiones")
        print("9. Salir")
        opcion = input("Seleccione una opción")

        if opcion == '1':
            DNI = input("Nombre del estudiante: ")
            nombre = input("Nombre del esudiante: ")
            edad = input("Nombre del esudiante: ")
            fecha_de_nacimiento = input("Nombre del esudiante: ")
            apellido = input("Nombre del esudiante: ")
            estado = input("Nombre del esudiante: ")
            curso = input("Nombre del esudiante: ")
            Estudiante.guardar(DNI, nombre, edad, fecha_de_nacimiento, apellido, estado, curso)
        if opcion == '2':
            nombre = input("Nombre del esudiante: ")
            nombre = input("Nombre del esudiante: ")
            nombre = input("Nombre del esudiante: ")
            
        if opcion == '3':
            nombre = input("Nombre del esudiante: ")
            nombre = input("Nombre del esudiante: ")
        if opcion == '4':
            nombre = input("Nombre del esudiante: ")
            nombre = input("Nombre del esudiante: ")
        if opcion == '5':
            nombre = input("Nombre del esudiante: ")
        if opcion == '6':
            nombre = input("Nombre del esudiante: ")
        if opcion == '7':
            nombre = input("Nombre del esudiante: ")
        if opcion == '8':
            nombre = input("Nombre del esudiante: ")
        if opcion == '9':
            nombre = input("Nombre del esudiante: ")
            print("saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente nuevamente.")

    conn.close()

if __name__ =='__main__':
    main()