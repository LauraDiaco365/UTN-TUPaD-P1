# 
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print (moda)
print (mediana)
print (media)
if (media > mediana) and (mediana > moda):
    print ("Hay sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print ("Hay sesgo negativo")
else:
   if media == mediana ==moda:
    print("No hay sesgo")