# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numerosUsuario= []
cantidadNumeros=100
contador= 0
pares= 0
impares =0
positivos= 0
negativos =0
while contador != cantidadNumeros:
    numerosUsuario.append( int (input("Ingrese un numero entero: ")))
    contador= contador + 1
    print (numerosUsuario)
for numero in numerosUsuario:
    if numero %2 == 0:
        pares= pares +1
    elif numero % 2 != 0:
        impares= impares +1 
    if numero >= 0:
        positivos= positivos+1
    elif numero < 0:
        negativos= negativos+1
print (f"De los numeros ingresados \n {positivos} son positivos \n {negativos} son negativos \n {pares} son pares \n {impares} son impares")