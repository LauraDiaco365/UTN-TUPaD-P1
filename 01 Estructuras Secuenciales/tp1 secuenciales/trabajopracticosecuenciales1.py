# 1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre= input("Ingrese su nomnbre: ")
apellido= input ("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
residencia= input("Ingrese su lugar de residencia: ")
print( f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {residencia} ")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= int (input("Ingrese el radio del circulo: "))
area= 3.14 * (radio **2)
perimetro= 2* 3.14* radio
print (f"El area de circulo es {area} y su perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos=int(input("Ingrese la cantidad de segundos: "))
hora= segundos /3600
print (f"La cantidad de segundos ingresados equivale a {hora} horas ")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número
numero= int(input("Ingrese un numero: "))
uno= numero *1
dos= numero *2
tres= numero*3
cuatro= numero *4
cinco= numero *5
seis= numero *6
siete= numero *7
ocho= numero *8
nueve= numero *9
diez= numero *10
print(f"La tabla de multiplicar del {numero} es la siguiente:")
print (f" {numero} x 1= {uno}")
print (f" {numero} x 2= {dos}")
print (f" {numero} x 3= {tres}")
print (f" {numero} x 4= {cuatro}")
print (f" {numero} x 5= {cinco}")
print (f" {numero} x 6= {seis}")
print (f" {numero} x 7= {siete}")
print (f" {numero} x 8= {ocho}")
print (f" {numero} x 9= {nueve}")
print (f" {numero} x 10= {diez}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1= int(input("Inngrese un numero distinto de cero: "))
numero2= int(input("Inngrese un numero distinto de cero: "))

suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2

print(f"El numero {numero1} + {numero2} = {suma}")
print(f"El numero {numero1} - {numero2} = {resta}")
print(f"El numero {numero1} x {numero2} = {multiplicacion}")
print(f"El numero {numero1} / {numero2} = {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) 2
altura= float (input("Ingrese su altura en mts: "))
peso= float (input ("Ingrese su peso en kg: "))

imc= peso / (altura **2)

print(f"Su indice de masa corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 95. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius= float (input("Ingrese una temperatura en grados Celsius: "))
fahrenheit= 1.8 * celsius + 32
print (f"La temperatura ingresada en Celsius equivale a {fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1= int (input("Ingrese un numero: "))
numero2=int (input("Ingrese un segundo numero: "))
numero3= int (input("Ingrese un tercer numero: "))

promedio= (numero1 + numero2 + numero3) / 3 
print (f"EL promedio de los 3 numeros ingresados es: {promedio}")



