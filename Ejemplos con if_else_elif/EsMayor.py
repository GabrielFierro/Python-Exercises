# Algoritmo que le solicita al usuario que ingrese su edad y le muestra por pantalla si es mayor
# de edad o menor

"Zona de declaración e inicialización de variable"

edad = 0

print("Ingrese su edad")
edad = int(input())

if edad>=18:
	print("Es mayor de edad")
else:
	print("Es menor de edad")
