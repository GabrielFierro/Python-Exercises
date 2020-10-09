#Algoritmo que solicita al usuario el valor de una compra, le aplica un descuento de 15% y muestra el resultado final por consola.

# Zona de inicialización de variables
descuento = 0.15

print("Ingrese el valor final de la compra")
valorCompra = float(input())

valorFinal = valorCompra - (valorCompra*descuento)

print ("El valor de la compra con un descuento de " + str(descuento) + " porciento es " + str(valorFinal))