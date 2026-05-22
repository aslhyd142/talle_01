import random

# Generar número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

intento = int(input("Adivina el número entre 1 y 10: "))

print("Adivina el número entre 1 y 10")

while intento != numero_secreto:

    intento =2

    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
    elif intento > numero_secreto:
        print("El número a adivinar es mayor.")
        break
    else:
        print("El número a adivinar es menor.")
        break