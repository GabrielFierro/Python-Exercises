import math

# Algoritmo que determina la norma de un vector definido en R2

def calcular_norma(x,y):

    # Función que dados dos valores que recibe por parámetro, calcula la norma del vector y retorna el resultado.
    
    discriminante = (x*x) + (y*y)

    norma = math.sqrt(discriminante)

    return norma


print('Ingrese el valor de la primer componente del vector')
primer_componente = float(input())

print('Ingrese el valor de la segunda componente del vector')
segunda_componente = float(input())

resultado = calcular_norma(primer_componente, segunda_componente)

print ("La norma del vector ("+str(primer_componente)+","+str(segunda_componente)+") es: {}".format(resultado))