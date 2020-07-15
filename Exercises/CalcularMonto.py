# Algoritmo que determina el dinero que obtendrá el vendedor a partir del sueldo base, más un 10% por sus 3 comisiones de ventas. Muestra el resultado por consola.

# Zona de inicialización de variables.
sueldoBase = 0.0
venta = 0.0
unaVenta = 0.0
otraVenta = 0.0
comisionFinal = 0.0
totalARecibir = 0.0

print("Ingrese el valor de su sueldo base")
sueldoBase = float(input())

print("Ingrese el valor de la 1er venta")
venta = float(input())

print("Ingrese el valor de la 1er venta")
unaVenta = float(input())

print("Ingrese el valor de la 1er venta")
otraVenta = float(input())

comisionFinal = (venta*0.1) + (unaVenta*0.1) + (otraVenta*0.1)

totalARecibir = sueldoBase + comisionFinal

print("El valor final a recibir es " + str(totalARecibir))

