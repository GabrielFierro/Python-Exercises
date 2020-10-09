# Algoritmo que determina el dinero que obtendrá el vendedor a partir del sueldo base, más un 10% por sus 3 comisiones de ventas. 
# Muestra el resultado por consola.

print("Ingrese el valor de su sueldo base")
sueldoBase = float(input())

print("Ingrese el valor de la primera venta")
primera_venta = float(input())

print("Ingrese el valor de la segunda venta")
segunda_venta = float(input())

print("Ingrese el valor de la tercera venta")
tercera_venta = float(input())

comisionFinal = (primera_venta*0.1) + (segunda_venta*0.1) + (tercera_venta*0.1)

totalARecibir = sueldoBase + comisionFinal

print("El valor final a recibir es " + str(totalARecibir))
