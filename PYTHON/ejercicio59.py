numero_secreto = 7

for intento in range(5):
    numero = int(input("Adivine el número: "))

    if numero == numero_secreto:
        print("Ganaste")
        break
else:
    print("Perdiste")