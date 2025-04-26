# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

lista= []

for numero in range (1, 101):
    if numero % 4 ==0:
        lista.append (numero)
print (lista)