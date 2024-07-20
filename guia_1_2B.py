# Crea un programa que pueda sumar los numeros pares comprendidos entre el 1 y el 10.

pares= 0
impares= 0

numero= int(input("Escriba un numero entre el 1 y el 10, o 0 para terminar: "))

while numero !=0:
    if numero % 2 == 1:
        impares += 1
    else: 
        pares += 1 
    numero= int(input("Escribe otro numero entre 1 y 10, o 0 para terminar: "))

print("El total de numeros pares es: ", pares)
print("El total de numeros impares es: ", impares)