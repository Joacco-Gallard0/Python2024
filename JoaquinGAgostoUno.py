menu = """
******************************************
*1- Introducir notas de matematicas      *
*2- Mostrar promedio y cantidad de notas *   
*3- Salir                                *              
******************************************
"""

notas = []
contador = 0

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones: "))
    if opcion == 1:
        nota = int(input(f"introduce las notas de matematicas: "))
        if 0 < nota < 11:
            notas.append(nota)
            contador = contador + 1
        else:
            print("No es un valor válido")
            continue

    if opcion == 2:
        if len(notas) > 0:
            suma = sum(notas)
        print(f"La suma de las notas es: {suma}")
    
    if opcion == 3:
       print("Nos vemo, chau")
       break
    
print("FIN")