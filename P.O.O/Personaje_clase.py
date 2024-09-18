class Personaje:
    #atributo de clase
    estado = True
    vida = 100

    #constructor / atributo de instancia
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad 
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado
        self.vida = Personaje.vida  
        
    def atacar(self, otro_personaje):
        if self.estado:
            danio = self.fuerza - (otro_personaje.resistencia)
            print(f"{self.nombre} atacar a {otro_personaje.nombre} causando {danio} de daño")
            otro_personaje.recibir_dano(danio)
        else:   
            print(f"{self.nombre} esta muerto y no puede atacar.")
    
    def recibir_dano(self, cantidad):
        if self.estado:
            self.vida = self.vida - cantidad
    
    def mostrar_info(self): 
        print

    