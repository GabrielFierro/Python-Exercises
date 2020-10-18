# Algoritmo que dada unca cadena de caracteres que el usuario ingresa, invoca a la funcion remover_vocales.

def remover_vocales(cadena):

    # Función que dada una cadena de caracteres que recibe por parámetro, determina si posee vocales y en caso afirmativo, procede a eliminar las vocales.
    
    # Zona de inicialización de variable
    vocales = 'aeiouAEIOU' # Declaro una variable con las vocales

    for v in vocales:
        cadena = cadena.replace(v, '')

    return cadena


# Ingreso de datos por parte del usuario

print('Ingrese una cadena de caracteres de la que desea sacar sus vocales')

palabra = input()

resultado = remover_vocales(palabra)

print('La palabra ingresada',palabra,'sin caracteres resulta',resultado)