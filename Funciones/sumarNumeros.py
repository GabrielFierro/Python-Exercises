# Algoritmo que invoca a la función suma con una lista junto a su longitud como sus argumentos.

def suma(lista_de_numeros, longitud_lista):

    '''
    Función que dada una lista de elementos junto a su longitud que recibe por parámetro,
    suma los elementos que dicha lista posee y, retorna el resultado.
    '''

    if longitud_lista == 0:
        resultado = lista_de_numeros[0]
    else:
        resultado = suma(lista_de_numeros,longitud_lista-1) + lista_de_numeros[longitud_lista]  # Invocación recursiva

    return resultado

"Zona de declaración e inicialización de variables"

resultado = 0
lista_de_numeros = [2,7,4,23,77,14]
longitud = len(lista_de_numeros)-1

print('La suma de los números de la lista es:',suma(lista_de_numeros,longitud))