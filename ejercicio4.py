#definir funciones
def calcular_area_circulo(radio):
    area= 3.14 * radio **2
    return area
def perimetro_circulo(radio):
    perimetro=2 * 3.14 * radio
    return perimetro

#programa principal
radio= int(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)} y el perimetro es: {perimetro_circulo(radio)} ")