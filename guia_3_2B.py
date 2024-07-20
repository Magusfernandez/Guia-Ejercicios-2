# Crear un programa que solicite al usuario que ingrese un numero.
# Se debera validar que se encuentre entre 0 y 9 inclusive.
# En caso de no coincidir con el rango, volverlo a solicitar hasta que la condicion se cumpla.

numero= int(input("Escriba un numero entre 0 y 9: "))

while numero < 0 or numero >9:
    print("Su numero no es valido")
    numero =int(input("Pruebe ingresando otro numero: "))

print("Su numero si es valido!!")