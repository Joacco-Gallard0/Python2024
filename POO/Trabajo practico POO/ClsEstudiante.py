import sqlite3
from sqlite3.dbapi2 import connect

class Estudiante:
    def __init__(self, DNI, nombre, edad, fecha_de_nacimiento, apellido, estado, curso):
        self.DNI = DNI
        self.nombre = nombre
        self.edad = edad 
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.apellido = apellido
        self.estado = estado
        self.curso = curso

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes (DNI, nombre, edad, fecha_de_nacimiento, apellido, estado, curso) VALUES (?, ?, ?)',(self.nombre_id, self.edad, self.año_id))
        
        conn.commit()
        conn.close()

@staticmethod
def obtener_estudiantes():
    conn =sqlite3.connect('escolar.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Estudiantes')
    estudiantes = c.fetchall()
    conn.close()

    return estudiantes