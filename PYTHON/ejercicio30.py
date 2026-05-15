usuario=input("ingrese su usuario:")
contrasena=input("ingrese su contraseña:")
rol=input("ingrese su rol:")

if(usuario=="admin" and contrasena=="1234" and rol=="administrador"):
    print("bienvenido admin")

elif(usuario=="admin" and contrasena=="1234" and rol!="administrador"):
    print("bienvenido admin pero no tienes permisos de administrador")

else:
    print("usuario o contraseña incorrectos")
