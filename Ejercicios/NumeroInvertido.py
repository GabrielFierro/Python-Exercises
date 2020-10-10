# Algoritmo que dado un número de dos cifras, invierte dicho número y lo muestra por consola.

print("Ingrese el número que desea invertir")
numero = int(input())

unidad = numero // 10 # Almacena en la variable unidad el penúltimo dígito
decena = numero % 10 # Almacena en la variable el último dígito

print("El número " + str(numero) + " invertido es " + str(decena) + str(unidad))
