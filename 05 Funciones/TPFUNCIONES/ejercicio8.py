def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicitar los datos al usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular IMC y mostrar el resultado con dos decimales
imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")