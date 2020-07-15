# Algoritmo que dada una variable inicializada con el valor cero, muestre que valores son pares y cuales impares utilizando la estructura while.

numero = 0

while numero <= 5:
    if numero % 2 == 0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")
    numero += 1