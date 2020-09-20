import math
# Algoritmo que le solicita al usuario que ingrese 2 pares ordenados de números pertenecientes al plano y calcula la distancia entre ambos.

# Zona de inicialización de variables
a = 0  # <=> x1
b = 0  # <=> y1
c = 0  # <=> x2
d = 0  # <=> y2
distancia = 0.0

print("Ingrese el valor de la primer coordenada correspondiente al punto P")
a = int(input())

print("Ingrese el valor de la segunda coordenada correspondiente al punto P")
b = int(input())

print("Ingrese el valor de la primer coordenada correspondiente al punto Q")
c = int(input())

print("Ingrese el valor de la segunda coordenada correspondiente al punto Q")
d = int(input())

distancia = math.sqrt(((c-a)**2) + ((d-b)**2))

print("La distancia entre los puntos es: " + str(distancia))
