# Crea un programa que solicite al usuario que ingrese una contraseña mediante prompt.
#Comprobar que la contraseña ingresada sea "utn750". 
#En caso de no coincidir, volver a solicitarla hasta que coincida.


contraseña= str(input("Crea una contraseña: "))

while contraseña != "utn750":
    print("La contraseña ingresada es incorrecta")
    contraseña= input("Ingresa la contraseña nuevamente:")
    
    if contraseña == "utn750":
        print("Contraseña correcta.")    
