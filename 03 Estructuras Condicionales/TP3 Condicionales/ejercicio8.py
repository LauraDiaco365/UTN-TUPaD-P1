#  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas

nombre= str (input("Ingrese su nombre: "))
opcion= int(input ("MENU \n 1. Si quiere su nombre en mayúsculas \n 2. Si quiere su nombre en minúsculas \n 3. Si quiere su nombre con la primera letra mayúscula \n Seleccione la opcion deseada: "))

while opcion != 0:    
    if opcion == 1:
        print (nombre.upper())
        break
    elif opcion == 2:
        print (nombre.lower())
        break
    elif opcion == 3:
        print (nombre.title())
        break
else:
    print ("Error! vuelva a ingresar la opcion")
    