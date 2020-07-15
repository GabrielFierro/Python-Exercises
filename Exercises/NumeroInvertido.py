# Algoritmo que dado un número de dos cifras, invierte dicho número y lo muestra por consola.

# Zona de inicialización de variables
numero = 0
decena = 0
unidad = 0

print("Ingrese el número que desea invertir")
numero = int(input())

unidad = numero // 10 # Almacena en la variable unidad el penúltimo dígito
decena = numero % 10 # Almacena en la variable el último dígito

print("El número " + str(numero) + " invertido es " + str(decena) + str(unidad))
