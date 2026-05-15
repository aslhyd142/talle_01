edad=int(input("ingrese su edad: "))
if edad<=12:
    print("niño")
elif edad>=13 and edad<=17:
    print("joven")
elif edad>=18 and edad<=59:
    print("adulto")
else:
    print("adulto mayor")