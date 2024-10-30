import sqlite3
from sqlite3.dbapi2 import connect

class Calificacion:
    def __init__(self, estudiante_id, materia_id, nota):
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.nota = nota

    def guardar(self):
        conn = sqlite3.connect("escolar.db")
        c = conn.cursor()

        c.execute('INSERT INTO Calificaiones (estudiante_id, materia_id, nota) VALUES (?, ?, ?)',(self.estudiante_id, self.materia_id, self.nota))
        
        conn.commit()
        conn.close()

@staticmethod
def obtener_Calificaciones():
    conn =sqlite3.connect('escolar.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM Calificaciones')
    calificaciones = c.fetchall()
    conn.close()

    return calificaciones