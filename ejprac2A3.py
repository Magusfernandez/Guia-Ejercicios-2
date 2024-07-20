# Crea un programa que a partir del ingreso de la altura de un basquetbolista determinar si es pivot o no.
# Para serlo el mismo debera medir mas de 1.80 metros.


altura= float(input("Ingrese su altura: "))

if altura < 1.80:
    print("Usted no es pivot.")
else:
    print("Usted es pivot!")