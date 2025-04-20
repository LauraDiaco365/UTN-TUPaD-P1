#  Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase= str(input("Ingrese su frase o palabra: "))
largo_frase= len(frase)
vocal=frase[largo_frase-1]
if vocal == "a" or vocal =="e" or vocal == "i" or vocal == "o" or vocal == "u":
    print (f"{frase} !")
else:
    print (frase)
