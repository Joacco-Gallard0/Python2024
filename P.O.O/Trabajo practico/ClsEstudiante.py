import sqlite3
from sqlite3.dbapi2 import connect

class Estudiante:
    def __init__(self, nombre, edad, año_id):
        self.nombre = nombre
        self.edad = edad 
        self.año_id = año_id

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes (nombre, edad, año_id) VALUES (?, ?, ?)',(self.nombre, self.edad, self.año_id))
        
        conn.commit()
        conn.close()

@staticmethod
def obtener_estudiantes():
    conn =sqlite3.connect('escolar.db')