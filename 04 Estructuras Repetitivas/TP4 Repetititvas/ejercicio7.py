# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

sumatoria= 0
numero1= 0
numero2= int (input("Ingrese el numero hasta el cual desea sumar: "))


while numero1 < numero2:
    numero1= numero1 + 1
    sumatoria=sumatoria+numero1
    print (sumatoria)
