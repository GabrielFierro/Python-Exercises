# Algoritmo que dado un rango de números, el usuario ingresa dígitos y muestra por consola la cantidad de números pares que hay dentro del rango.

# Zona de inicialización de variables
numero = 0
contador = 0
modulo = 0

for var in range(1,5):
	
	print("Ingrese un número")
	numero = int(input())

	modulo = numero % 2

	if modulo == 0:
		contador = contador + 1

print("Ingresó " , contador , " números pares")
