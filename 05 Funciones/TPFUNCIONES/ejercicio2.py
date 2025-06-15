#definicion de variables
def saludar_usuario (nombre):
    print(f"Hola {nombre}!")
    return nombre

#Programa principal
nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)