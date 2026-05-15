lado1=int(input("ingrese el valor del lado 1: "))
lado2=int(input("ingrese el valor del lado 2: "))
lado3=int(input("ingrese el valor del lado 3: "))
if(lado1==lado2 and lado2==lado3 ):
    print("el triangulo es equilatero")
elif(lado1==lado2 or lado3==lado1):
    print("el triangulo es isóceles")

else: print("el triangulo es escaleno")
