class Personaje:
    #atributo de clase
    estado = True
    vida = 100

    #constructor / atributo de instancia
    def __init__ (self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad 
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado
        self.vida = Personaje.vida  
        
    def atacar(self, otro_personaje):   
        if  self.estado:
            danio = self.fuerza - (otro_personaje.resistencia)
            print(f"{self.nombre} atacar a {otro_personaje.nombre} causando {danio} de daño")
            otro_personaje.recibir_dano(danio)

            danio = self.vida -otro_personaje.resistencia 
            if danio >= 0:
                self.vida = self.vida - danio
        else:   
            print(f"{self.nombre} esta muerto y no puede atacar.")

        

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0  
            self.estado = False
            print (f"{self.nombre} ha muerto")
        
    def mostrar_info(self): 
        print   
    
    
    