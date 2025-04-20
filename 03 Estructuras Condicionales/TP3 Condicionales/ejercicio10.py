# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= str(input("Ingrese el hemisferio en que se encuetra con la letra inicial (Norte o Sur): "))
mes= int (input ("Ingrese el mes del año: "))
dia= int (input("Ingrese el dia: "))


while hemisferio.upper() == "N":
    if mes == 1 or mes == 2:
        print ("Usted se encuentra en Invierno")
        break
    elif mes == 12 and dia >= 21:
        print ("Usted se encuentra en Invierno")
        break
    elif mes== 3 and dia <= 20:
        print ("Usted se encuentra en Invierno")
        break
    elif mes == 3 and dia >=21:
        print ("Usted se encuentra en Primavera")
        break
    elif mes== 4 or mes == 5:
        print ("Usted se encuentra en Primavera")
        break
    elif mes == 6 and dia <=20:
        print ("Usted se encuentra en Primavera")
        break
    elif mes ==6 and dia >=21:
        print ("Usted se encuentra en Verano")
        break
    elif mes == 7 or mes == 8:
        print ("Usted se encuentra en Verano")
        break
    elif mes == 9 and dia <= 20:
        print ("Usted se encuentra en Verano")
        break
    elif mes == 9 and dia >= 21:
        print ("Usted se encuentra en Otoño")
        break
    elif mes == 10 or mes== 11:
        print ("Usted se encuentra en Otoño")
        break
    elif mes == 12 and dia <=20:
        print ("Usted se encuentra en Otoño")
        break
    
while hemisferio.upper() == "S":
    if mes == 1 or mes == 2:
        print ("Usted se encuentra en Verano")
        break
    elif mes == 12 and dia >= 21:
        print ("Usted se encuentra en Verano")
        break
    elif mes== 3 and dia <= 20:
        print ("Usted se encuentra en Verano")
        break
    elif mes == 3 and dia >=21:
        print ("Usted se encuentra en Otoño")
        break
    elif mes== 4 or mes == 5:
        print ("Usted se encuentra en Otoño")
        break
    elif mes == 6 and dia <=20:
        print ("Usted se encuentra en Otoño")
        break
    elif mes ==6 and dia >=21:
        print ("Usted se encuentra en Invierno")
        break
    elif mes == 7 or mes == 8:
        print ("Usted se encuentra en Invierno")
        break
    elif mes == 9 and dia <= 20:
        print ("Usted se encuentra en Invierno")
        break
    elif mes == 9 and dia >= 21:
        print ("Usted se encuentra en Primavera")
        break
    elif mes == 10 or mes== 11:
        print ("Usted se encuentra en Primavera")
        break
    elif mes == 12 and dia <=20:
        print ("Usted se encuentra en Primavera")
        break