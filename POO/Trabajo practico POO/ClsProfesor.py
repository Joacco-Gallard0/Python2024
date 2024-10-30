import sqlite3
from sqlite3.dbapi2 import connect

class Profesor:
    def __init__(self, nombre, apellido, profesor_id, curso, materia):
        self.nombre = nombre
        self.apellido = apellido 
        self.profesor_id = profesor_id
        self.materia_id = materia
        self.curso = curso

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Profesores (nombre, apellido, profesor_id, curso, materia) VALUES (?, ?, ?)',(self.nombre, self.apellido,self.profesor_id, self.curso, self.materia))
        
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