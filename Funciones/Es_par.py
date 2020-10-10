# Algoritmo que invoca a la función es_par() pasandole como argumento un número, luego la función verifica si es par o impar el número.

def es_par(num):

    # Función que dado un elemento que recibe por parámetro, determina si es par o no, y retorna una cadena de caracteres.
    
    if num % 2 == 0:
        res = 'El numero es par'
    else:
        res = 'El numero no es par'
    return res

print(es_par(2)) # Muestra por consola el resultado de invocar a la funcion es_par con el argumento 2
print(es_par(11)) # Muestra por consola el resultado de invocar a la funcion es_par con el argumento 11