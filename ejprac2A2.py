# Crear un programa que pida al usuario un numero y pueda calcular si es o no, mayor de edad.
# Si es mayor de 18 años se mostrará el mensaje "MAYOR" caso contrario "MENOR".

edadus= int(input("Ingrese su edad: "))

if edadus>= 18:
    print("MAYOR")
else: 
    print("MENOR")