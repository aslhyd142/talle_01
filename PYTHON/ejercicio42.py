numeros = []
suma = 0

n = int(input("Cantidad de números: "))

for i in range(n):
    num = int(input("Ingrese un número: "))
    numeros.append(num)
    suma += num

print("Suma:", suma)