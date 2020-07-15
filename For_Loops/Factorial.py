# Algoritmo que dado un número ingresado por el usuario, determina su factorial y muestra el resultado por consola.

# Zona de inicialización de variables

numero = 0
resultado = 1
inicio = 1
i = 1
acumulador = 0

print("Ingrese un número para averiguar su factorial")
numero = int(input())

for i in range(inicio, numero+1):
	resultado = resultado*i	

print("El factorial del número ", numero, " es ", resultado)