import sqlite3
from sqlite3.dbapi2 import connect

class Materia:
    def __init__(self, nombre, materia_id, curso):
        self.nombre = nombre
        self.materia_id = materia_id
        self.curso = curso

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Materias (nombre, materia_id, curso) VALUES (?, ?, ?)',(self, self.nombre, self.materia_id, self.curso))
        
        conn.commit()
        conn.close()

@staticmethod
def obtener_Materias():
    conn =sqlite3.connect('escolar.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Materias')
    materias = c.fetchall()
    conn.close()

    return materias