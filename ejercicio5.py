#definicion de funciones
def segundos_a_horas(segundos):
    horas= segundos/ 3600
    return horas

#programa principal
segundos= int(input("Ingrese la cantidad de segundos a convertir en horas: "))
print(f"La cantidad de horas a la que equivalen {segundos} segundos es {segundos_a_horas(segundos)} horas")