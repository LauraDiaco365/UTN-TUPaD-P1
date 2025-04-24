# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero= str (input("Ingrese un numero: "))
largoNum= len (numero)
numeroinvertido= ""

for i in range ((largoNum) -1, -1, -1):
    numeroinvertido= numeroinvertido + numero [i]
print (f" El numero invertido es: {numeroinvertido}" )