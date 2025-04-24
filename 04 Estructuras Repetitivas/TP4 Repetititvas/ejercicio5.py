# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
contador= 1
numeroAdivinar= 5

numero= int (input(f"Intento {contador} Intente adivinar el numero de 0 a 9: "))

while numero != numeroAdivinar:
    contador= contador + 1
    numero= int (input(f"Intento {contador} Intente nuevamente adivinar el numero de 0 a 9: "))
else:
    print (f"Has adivinado el numero era {numeroAdivinar} y te llevo {contador} intentos!")

    