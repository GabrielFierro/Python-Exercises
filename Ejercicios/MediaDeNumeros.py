# Algoritmo que le solicita al usuario el valor de 3 números y calcula la media con respecto a los valores ingresados, y muestra el resultado por consola.

print("Ingrese el valor del numero")
numero = int(input())

print("Ingrese el valor de un numero")
unNumero = int(input())

print("Ingrese el valor del otro numero")
otroNumero = int(input())

media = (numero + unNumero + otroNumero)/3

print("La media con respecto a los números " + str(numero) + ", " + str(unNumero) + " y " + str(otroNumero) + " es " + str(media))
