import sqlite3
from sqlite3.dbapi2 import connect

class Profesor:
    def __init__(self, DNI, nombre, apellido, curso, materia):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido 
        self.materia_id = materia
        self.curso = curso

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Profesores (DNI, nombre, apellido, curso, materia) VALUES (?, ?, ?)',(self.DNI, self.nombre, self.apellido, self.curso, self.materia))
        
        conn.commit()
        conn.close()

@staticmethod
def obtener_profesores():
    conn =sqlite3.connect('escolar.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Profesores')
    profesores = c.fetchall()
    conn.close()

    return profesores