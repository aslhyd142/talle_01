n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: "))
if(n1<n2 and n1<n3):
    print("El orden ascendente es: " + str(n1) + ", " + str(n2) + ", " + str(n3))

elif(n2<n1 and n2<n3):
    print("El orden ascendente es: " + str(n2) + ", " + str(n1) + ", " + str(n3))

elif(n3<n1 and n3<n2):
    print("El orden ascendente es: " + str(n3) + ", " + str(n1) + ", " + str(n2))
