# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista= []

for numero in range (10,31, 5):
    lista.append (numero)
    print(lista)
print (lista [0], lista [1])
