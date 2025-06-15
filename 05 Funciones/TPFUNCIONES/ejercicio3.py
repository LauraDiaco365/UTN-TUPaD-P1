#definicion de variables
def informacion_personal (nombre,apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return nombre, apellido, edad, residencia

#programa principal
nombre= input("Ingrese su nombre: ")
apellido= input ("Ingrese su apellido: ")
edad= input ("Ingrese su edad: ")
residencia= input("Ingrese su lugar de residencia: ")
informacion_personal (nombre,apellido, edad, residencia)