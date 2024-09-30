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
    
def mostrar_personajes():
    if cantidadPersonaje == 0:
        print("No hay personajes creados")

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones:  "))
    
    if opcion == 1:
        nombre = input("Ponle un nombre a tu personaje: ")
        altura = int(input("Ingrese una altura deseada del personaje (cm): "))
        velocidad = int(input("Añada una velocidad que desea: "))
        resistencia = int(input("Agrege la resistencia que desea: "))
        fuerza = int(input("Ahora por ultimo pongale una fuerza deseada: "))
    
        nuevo_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza)

        personajes.append(nuevo_personaje)

        cantidadPersonaje += 1
        print(f"El personaje {nuevo_personaje.nombre} ha sido creado con exito")
        print(f"Cantidad de personajes creados para jugar: {cantidadPersonaje}")
    
    
    elif opcion == 2:
        if cantidadPersonaje < 2:
            print("Se necesita dos personajes para poder jugar")
        else:
            print("Iniciando la carrera con los siguientes personajes:")
            mostrar_personajes()
        
        atacante_idx = int(input("Seleccione el numero del personaje atacante que desea jugar: ")) - 1
        defensor_idx = int(input("Seleccione el numero del personaje defensor que desea jugar: ")) - 1

        if 0 <= atacante_idx < cantidadPersonaje and 0<= defensor_idx < cantidadPersonaje:
            atacante = personajes[atacante_idx]
            defensor = personajes[defensor_idx]

            if atacante.estado and defensor.estado:
                atacante.atacar(defensor)
            else:
                print("Uno o ambos personajes estan muertos y no podran pelear")
        else:
            print("Seleccione incorrecta. Pruebe de nuevo")
        
        print("\nEstado actualizado de los personajes: ")
        mostrar_personajes()


    elif opcion == 3:
        print("Game over")
        break
    
    else:
        print("Opción incorrecta, pruebe otra vez")
        




