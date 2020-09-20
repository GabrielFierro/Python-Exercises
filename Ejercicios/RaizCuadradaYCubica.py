import math

# Algoritmo que le solicita al usuario que ingrese un número, y muestra por consola la raíz cuadrada y cúbica respectivamente, del valor ingresado.

# Zona de inicialización de variables
numero = 0
raizCuadrada = 0.0
raizCúbica = 0.0

print("Ingrese un número")
numero = int(input())

raizCuadrada = math.sqrt(numero)

raizCubica = math.ceil(numero**(1/3))

print("La raiz cuadrada del número " + str(numero) + " es: " + str(raizCuadrada)) # Muestra por pantalla el valor de la raiz cuadrada del número ingresado por el usuario

print("La raiz cúbica del número " + str(numero) + " es: " + str(raizCubica)) # Muestra por pantalla el valor de la raíz cúbica del número ingresado por el usuario