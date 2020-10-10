# Algoritmo que contiene ejemplos de while anidados con condicionales if-else-elif
# El algoritmo le solicita al usuario que ingrese la palabra 'empezar' para operar con un menú de opciones.

inicio = input("Escribe empezar para iniciar el programa: ")

while (inicio == 'empezar'):
    print("Opcion 0: Finalizar el programa")
    print("Opción 1: Ingresar un número y saber si es par o impar")
    print("Opción 2: Ingresar un número y averiguar la potencia del mismo, elevado a la potencia 2")
    opcion = int(input())

    if opcion == 0:
        inicio = 'terminar'

    if opcion == 1:
        
        numero = int(input("Ingrese un número: "))
        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    
    elif opcion == 2:

        numero = int(input("Ingrese un número: "))
        print("La potencia del número",numero,"es",numero**2)
