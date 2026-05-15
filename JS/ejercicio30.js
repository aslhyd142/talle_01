usuario="admin"
contrasena="1234"
rol="administrador"

if(usuario=="admin" && contrasena=="1234" && rol=="administrador"){
    console.log("bienvenido admin")
}
else if(usuario=="admin" && contrasena=="1234" && rol!="administrador"){
    console.log("bienvenido admin pero no tienes permisos de administrador")
}
else{
    console.log("usuario o contraseña incorrectos")
}