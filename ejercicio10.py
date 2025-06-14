#definir variables
def calcular_promedio (a,b,c):
    suma= a+b+c
    promedio= suma/3
    return promedio

#programa principal
a= int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c= int(input("Ingrese el tercer numero: "))

print(f"El promedio de los tres numeros ingresados es: {calcular_promedio (a,b,c)}")