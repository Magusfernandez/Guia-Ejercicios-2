# Crear un programa que solicite 5 numeros mediante prompt. 
# Calcular la suma acumulada y el promedio de los numeros ingresados.

num1= int(input("Ingresa un numero: "))
num2= int(input("Ingresa un numero: "))
num3= int(input("Ingresa un numero: "))
num4= int(input("Ingresa un numero: "))
num5= int(input("Ingresa un numero: "))

suma= num1 + num2 + num3 + num4 + num5

print("La suma de los numeros ingresados es ",suma)

promedio= suma // 5

print("El promedio de esos mismos numeros es: ",promedio)