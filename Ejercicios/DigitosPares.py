# Algoritmo que dada una lista con valores cargados del 0 al 9, imprime los números pares que se encuentren dentro del rango que va de cero a la longitud final de dicha lista.

# Zona de inicialización de variables
lista_de_numeros = [0,1,2,3,4,5,6,7,8,9]
longitud = len(lista_de_numeros)

for lista_de_numeros in range(0,longitud,2):
	print(lista_de_numeros)
