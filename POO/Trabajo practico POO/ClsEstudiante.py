import sqlite3
from sqlite3.dbapi2 import connect

class Estudiante:
    def __init__(self, nombre, edad, estudiante_id, apellido, curso):
        self.nombre = nombre
        self.edad = edad 
        self.estudiante_id = estudiante_id
        self.apellido = apellido
        self.curso = curso

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes (nombre, edad, estudiante_id, apellido, curso) VALUES (?, ?, ?)',(self.nombre, self.edad, self.estudiante_id, self.apellido, self.curso))
        
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