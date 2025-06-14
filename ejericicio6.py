#definir variables
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#programa principal
numero= int (input("Ingrese el numero del cual deaea saber la tabla de multiplicar: "))
tabla_multiplicar(numero)