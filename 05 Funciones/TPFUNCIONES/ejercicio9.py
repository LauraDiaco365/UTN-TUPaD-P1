def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura en Celsius
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))

# Llamar a la función y mostrar el resultado
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f}")