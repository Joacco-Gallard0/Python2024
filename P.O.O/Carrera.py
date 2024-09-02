from Personaje_clase import Personaje

menu= '''
#########################################
#     1 - Calcular Area Triangulo       #
#     2 - Calcular Area Rectangulo      #
#     3 - Salir                         #
######################################### 
'''
print(menu)

cantidadPersonaje = 0

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones:  "))
    
    if opcion == 1:
    
        if opcion == 1:

                if opcion == 1:


p1 = Personaje
p1 = input(f"Ponle un nombre a tu personaje:{p1.nombre}")
p1 = input(f"Ingrese una altura deseada del personaje:{p1.altura}")
p1 = input(f"Añada una velocidad que desea:{p1.velocidad}")
p1 = input(f"Agrege la resistencia que desea:{p1.resistencia}")
p1 = input(f"Ahora por ultimo pongale una fuerza deseada:{p1.fuerza}")

print (f"El personaje se llama{p1.nombre}, su altura es de {p1.altura}, tiene una velocidad de {p1.velocidad}, una resistencia de {p1.resistencia} y fuerza de unos {p1.fuera}")
