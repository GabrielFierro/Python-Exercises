# Algoritmo que dada una lista con valores precargados, llama a la función 'mi_funcion' pasándole como argumento una lista y suma sus valores, retornando el resultado

def my_function(mi_lista):

    # Función que recibe por parámetro una lista, suma los elementos que posee y muestra el resultado por consola
    "Zona de inicialización de variable"
    cont = 0

    for cant in mi_lista:
        cont = cont + cant
    
    print('El resultado es:',cont)


def cant_elementos(my_list):

    # Función que recibe por parámetro una lista, y cuenta la cantidad de elementos que la misma posee. Retorna el resultado.
    "Zona de inicialización de variable"
    cont = 0
    
    for cant in my_list:
        cont = cont + 1
    
    return cont


"Zona de declaración e inicialización de variables"

lista1 = [2,13,11,6,0,7]
lista2 = [-1,5]

# Se le envía como argumento una lista 
my_function(lista1)  

# Se imprime por consola a la vez, que se llama a la función
print('La cantidad de números que posee la lista es:',cant_elementos(lista2))