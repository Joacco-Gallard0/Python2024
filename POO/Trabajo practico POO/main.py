import sqlite3
from ClsEstudiante import Estudiante, obtener_estudiantes
from ClsCalificación import Calificacion, obtener_Calificaciones
from ClsMateria import Materia, obtener_Materias
from ClsProfesor import Profesor, obtener_profesores

def conectar_db():
    conn = sqlite3.connect('escolar.db')
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
        opcion = input("Seleccione una opción:")

        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            estudiante_id = input("Id del estudiante: ")
            apellido = input("Apellido del estudiante: ")
            curso = input("Curso del estudiante: ")
            Estudiante.guardar(conn, nombre, edad, estudiante_id, apellido, curso)
        elif opcion == '2':
            nombre = input("Nombre del profesor: ")
            apellido = input("Apellido del profesor: ")
            profesor_id = input ("Id del profesor:")
            curso = input("Curso del profesor: ")
            materia = input("Materia que da el profesor: ")
            Profesor.guardar(conn, nombre, apellido, profesor_id, curso, materia)
        elif opcion == '3':
            nombre = input("Nombre de materia: ")
            materia_id = input("Id de materia: ")
            curso = input("De que curso es la materia: ")
            Materia.guardar(conn, nombre, materia_id, curso)
        elif opcion == '4':
            estudiante_id = input("Id del estudiante: ")
            materia_id = input("Id de materia: ")
            nota = input ("Ingrese la nota del estudiante: ")
            Calificacion.guardar(conn, estudiante_id, materia_id, nota)
        elif opcion == '5':
            obtener_estudiantes(conn)
        elif opcion == '6':
            obtener_profesores(conn)
        elif opcion == '7':
            obtener_Materias(conn)
        elif opcion == '8':
            obtener_Calificaciones(conn)
        elif opcion == '9':
            nombre = input("Nombre del esudiante: ")
            print("saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente nuevamente.")

    conn.close()

if __name__ =='__main__':
    main()