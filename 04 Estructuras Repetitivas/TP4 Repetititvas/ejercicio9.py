# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

numerosUsuarios=100
sumatoria= 0
contador= 0

while numerosUsuarios != contador:
     numeros= int (input("Ingrese un numero entero: "))
     contador= contador+1
     sumatoria =sumatoria+numeros
else:
    media= sumatoria/contador
    print (f"La media de los valores ingresados es: {media}")