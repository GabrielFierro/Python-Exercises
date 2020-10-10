# Algoritmo que dados dos vectores representados en R2, se aplicarán las operaciones de suma, producto por un escalar "k" y diferencia entre vectores.

def sumar_vectores(primer_componente_de_u, segunda_componente_de_u, primer_componente_de_v, segunda_componente_de_v):

    # Función que dados dos vectores recibidos por parámetro, suma componente a componente, y retorna un nuevo vector.

    x = primer_componente_de_u + primer_componente_de_v

    y = segunda_componente_de_u + segunda_componente_de_v

    vector = (x,y)

    return vector


print('Ingrese la primer componente del vector u')
primer_comp_de_u = float(input()) 
print('Ingrese la segunda componente del vector u')
segunda_comp_de_u = float(input()) 
print('Ingrese la primer componente del vector v')
primer_comp_de_v = float(input()) 
print('Ingrese la segunda componente del vector v')
segunda_comp_de_v = float(input()) 

resultado = sumar_vectores(primer_comp_de_u, segunda_comp_de_u, primer_comp_de_v, segunda_comp_de_v)

print("El resultado de sumar las componentes de los vectores ("+str(primer_comp_de_u)+","+str(segunda_comp_de_u)+") y ("+str(primer_comp_de_v)+","+str(segunda_comp_de_v)+") es: {}".format(resultado))