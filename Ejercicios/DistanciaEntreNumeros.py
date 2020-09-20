import math

#Algoritmo que pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

# Zona de inicialización de variables.
unNumero = 0
otroNumero = 0
resultado = 0
valorAbsoluto = 0

print("Ingrese un número")
unNumero = int(input())

print("Ingrese otro número")
otroNumero = int(input())

resultado = unNumero - otroNumero

valorAbsoluto = math.fabs(resultado) # Utiliza la función abs de la librería math, que determina el valor absoluto del valor que posee la variable resultado.

print("La distancia entre el número " + str(unNumero) + " y el número " + str(otroNumero) + " es " + str(valorAbsoluto))
