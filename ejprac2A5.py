# Crear un programa que al ingresar un numero pueda calcular si es mayor,
#niño/a (menor de 10) o pre-adolescente (edad entre 10 y 13 años)
#adolescente (edad entre 13 y 17 años) de edad.


edad= int(input("Ingrese su edad: "))

if edad <= 10:
    print("Eres un niño")
elif edad > 10 and edad <= 13:
    print("Eres pre-adolescente")
elif edad >=13 and edad < 17:
    print("Eres adolescente")
else: 
    print("Ya eres un adulto!")