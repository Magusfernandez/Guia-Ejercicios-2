# Crea un programa que solicite al usuario que ingrese una letra.
# Se debera validar que la letra sea "U", "T" o "N" (en mayusculas).
# En caso de no coincidir con ninguna de las letras, volver a solicitarla hasta que coincida.

letra= str(input("Ingresa una letra: "))

while letra != "U" and letra != "T" and letra != "N":
    print("La letra que ingresaste no es correcta!")
    letra= str(input("Intentalo de nuevo: "))

print("La letra que ingresaste es valida.")
