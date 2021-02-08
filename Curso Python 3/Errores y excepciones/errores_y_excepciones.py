def sumar(num1, num2):
    # Función que recibe por parámetro dos valores y retorna el resultado de sumarlos
    return num1+num2


def restar(num1, num2):
    # Función que recibe por parámetro dos valores y retorna el resultado de restarlos
    return num1-num2


def multiplicar(num1, num2):
    # Función que recibe por parámetro dos valores y retorna el resultado de multiplicarlos
    return num1*num2


def dividir(num1, num2):
    ''' Función que recibe por parámetro dos valores, divide ambos valores y retorna el resultado.
    En caso de encontrar un error actúa frente a ésto, mostrando dos carteles por consola.'''
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación no válida"


numero1 = int(input("Ingrese el primer número que desea operar: "))
numero2 = int(input("Ingrese el segundo número que desea operar: "))

operacion = input(
    "Ingrese la operación a realizar (sumar, restar, multiplicar, dividir): ")

if operacion == "sumar":
    print(sumar(numero1, numero2))

elif operacion == "restar":
    print(restar(numero1, numero2))

elif operacion == "multiplicar":
    print(multiplicar(numero1, numero2))

elif operacion == "dividir":
    print(dividir(numero1, numero2))
