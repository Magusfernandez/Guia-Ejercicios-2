# Crear un programa que se ingrese la edad del usuario 
# en numero y pueda calcular si es adolescente (edad entre 13 y 17 años)

edadusu= int(input("Ingrese su edad: "))

if edadusu >= 13 and edadusu < 17:
    print("Usted es un adolescente, no sabe lo que le espera.")
elif edadusu < 13:
    print("Usted aun es un niño, disfrutelo")
else: 
    print("Ya es un adulto, que comience el juego!")