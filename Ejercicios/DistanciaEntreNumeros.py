import math

# Algoritmo que pide al usuario dos números y muestra la distancia entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

print("Ingrese un número")
unNumero = int(input())

print("Ingrese otro número")
otroNumero = int(input())

resultado = unNumero - otroNumero

valorAbsoluto = math.fabs(resultado) # Utiliza la función abs de la librería math, que determina el valor absoluto del valor que posee la variable resultado.

print("La distancia entre el número " + str(unNumero) + " y el número " + str(otroNumero) + " es " + str(valorAbsoluto))
