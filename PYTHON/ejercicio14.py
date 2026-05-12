n1=int(input("numero1:"))
n2=int(input("numero2:"))
n3=int(input("numero3:"))
if n1>n2 and n1>n3:
    print("el numero mayor es:",  n1)

elif n2>n1 and n2>n3:
    print("el numero mayor es:",  n2)

elif n3>n1 and n3>n2:
    print("el numero mayor es:" , n3)

if n1==n2 and n2==n3:
    print("los numeros son iguales")