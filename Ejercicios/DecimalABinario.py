# Algoritmo que solicita al usuario que ingrese un valor decimal, y muestra por consola, su equivalente en números binarios.
# Luego, verifica la cantidad de ocurrencias del dígito 1 en dicho número binario.

def convertir_decimal(numero):

    # Función que dado un número entero como entrada, lo convierte en decimal y retorna el resultado
    cociente = numero // 2
    modulo = numero % 2
    resultado = ""

    if numero <= 2:
        resultado = str(cociente) + str(modulo)
    else:
        resultado = resultado + convertir_decimal(cociente) + str(modulo)

    return resultado


def contar_digitos(numero):

    # Función que recibe por parámetro un numero binario de tipo string y cuenta la cantidad de dígitos 1 que posee

    # Zona de inicialización de variables
    i = 0
    cont = 0

    for i in range(0, len(numero)):
        if numero[i] == '1':
            cont = cont + 1

    return cont


# Ingreso de datos para operar con la función convertir_decimal

print("Ingrese un número entero")
num = int(input())

res = convertir_decimal(num)    # Invocación de la función convertir_decimal

print("El número",num,"en binario es:",res)


# Ingreso de datos para operar con la función contar_digitos

print("Ingrese un número binario")
binario = input()

resultado = contar_digitos(binario)

print("La cantidad de dígitos 1 que posee el número binario",binario,"es:",resultado)
