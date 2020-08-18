# Algoritmo que dada una lista con valores precargados, llama a la función 'mi_funcion' pasándole como argumento una lista y suma sus valores, retornando el resultado

# Función con un parámetro de tipo Lista que muestra por consola la cantidad de valores que dicha lista posee
def my_function(my_list):
    
    cont = 0

    for x in my_list: 
        cont = cont + 1
    
    print('El resultado es:',cont)

# Función con un parámetro de tipo Lista que retorna la cantidad de elementos que dicha lista posee
def my_other_function(my_list):
    
    cont = 0
    
    for x in my_list:
        cont = cont + 1
    
    return cont

# Zona de inicialización de variables
lista1 = [2,13,11,6,0,7]
lista2 = [-1]

# Se le envía como argumento una lista 
my_function(lista1)  

# Se imprime por consola a la vez, que se llama a la función
print('La cantidad de números que posee la lista es:',my_other_function(lista2))