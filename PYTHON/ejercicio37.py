n=int(input("Ingrese un número: "))
fibonacci=0
fibonacci1=1
for i in range(1, n + 1):
    print("fibonacci: " + str(fibonacci))
    fibonacci2 = fibonacci + fibonacci1
    fibonacci = fibonacci1
    fibonacci1 = fibonacci2