palabra = str(input("Ingrese la palabra:"))
contador = 0
for i in palabra:
    if i == "a":
        print ("A", end="")
    elif i == "e":
        print ("E", end="")
    elif i == "i":
        print ("I", end="")   
    elif i == "o":
        print ("O", end="")   
    elif i == "u":
        print ("U", end="")       
    else:
        print (i, end="")