from Personaje_clase import Personaje

menu= '''
#########################################
#     1 - Crear personaje               #
#     2 - Jugar                         #
#     3 - Salir                         #
######################################### 
'''

cantidadPersonaje = 0
personajes = []

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones:  "))
    
    if opcion == 1:
        nombre = input("Ponle un nombre a tu personaje: ")
        altura = int(input("Ingrese una altura deseada del personaje (cm): "))
        velocidad = int(input("Añada una velocidad que desea: "))
        resistencia = int(input("Agrege la resistencia que desea: "))
        fuerza = int(input("Ahora por ultimo pongale una fuerza deseada: "))
    
        nuevo_personaje = Personaje(nombre, altura, velocidad, velocidad, resistencia, fuerza)
        personajes.append(nuevo_personaje)

        cantidadPersonaje += 1
        print(f"El personaje {nuevo_personaje.nombre} ha sido creado con exito")
        print(f"Cantidad de personajes creados para jugar: {cantidadPersonaje}")
    
    
    elif opcion == 2:
        if cantidadPersonaje == 0:
            print("No hay personajes creados para poder jugar")
        else:
            print("Iniciando la carrera con los siguientes personajes:")
            for personaje in personajes:
                print(f"*{personaje.nombre}")
        continue

    elif opcion == 3:
        print("Game over")
        break
    
    else:
        print("Opción incorrecta, pruebe otra vez")
        




