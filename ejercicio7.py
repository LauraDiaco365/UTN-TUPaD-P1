#definicion de variables
def operaciones_basicas (a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"

    return (suma, resta, multiplicacion, division) #creacion de tupla

# Solicitar al usuario los números
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

# Llamar a la función y mostrar los resultados
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

