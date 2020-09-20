# Ejercicio donde el usuario carga una nota numérica <= 10 y se muestra un mensaje por consola.

"Zona de declaración e inicialización de variable"

nota = float(input("Ingrese la nota: "))

if nota == 10:
    print("Promocionaste con excelente nota")
elif nota >= 8 and nota <= 10:
    print("Promocionaste") 
elif nota >=6 and nota <=7:
    print("Aprobaste, te faltó poco para promocionar")
else:
    print("Desaprobaste")

