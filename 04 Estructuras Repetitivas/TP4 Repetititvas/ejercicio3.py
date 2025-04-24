# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

sumatoria= 0
numero1= int(input("Ingrese un numero: "))
numero2= int (input("Ingrese otro numero: "))


while numero1 < numero2-1:
    numero1= numero1 + 1
    sumatoria=sumatoria+numero1
    print (sumatoria)
while numero2 < numero1 -1:
        numero2= numero2 + 1
        sumatoria=sumatoria+numero2
        print (sumatoria)
    