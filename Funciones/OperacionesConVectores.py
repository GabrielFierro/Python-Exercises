# Algoritmo que dados dos vectores representados en R2, se aplicarán las operaciones de suma, producto por un escalar "k" y diferencia entre vectores.

def sumar_vectores(primer_componente_de_u, segunda_componente_de_u, primer_componente_de_v, segunda_componente_de_v):

    # Función que dados dos vectores recibidos por parámetro, suma componente a componente, y retorna un nuevo vector.

    x = primer_componente_de_u + primer_componente_de_v

    y = segunda_componente_de_u + segunda_componente_de_v

    vector = (x,y)  # Le asigna a la variable vector, la tupla resultante de sumar las correspondientes componentes de los vectores

    return vector

def multiplicar_escalar(escalar, primer_componente, segunda_componente):

    # Función que recibe por parámetro un valor numérico junto a un vector, y multiplica dicho valor, con cada componente del vector

    x = primer_componente * escalar
    y = segunda_componente * escalar
    
    vector = (x,y) # Le asigna a la variable vector, los valores resultantes de muliplicar el escalar con cada componente

    return vector


'''
Ingreso de datos e invocación de la función sumar_vectores
'''

print('A continuación se ejecuta el algoritmo para sumar vectores'+'\n')

print('Ingrese la primer componente del vector u')
primer_comp_de_u = float(input()) 

print('Ingrese la segunda componente del vector u')
segunda_comp_de_u = float(input()) 

print('Ingrese la primer componente del vector v')
primer_comp_de_v = float(input()) 

print('Ingrese la segunda componente del vector v')
segunda_comp_de_v = float(input()) 

resultado = sumar_vectores(primer_comp_de_u, segunda_comp_de_u, primer_comp_de_v, segunda_comp_de_v) # Almacena en la variable resultado, la tupla resultante de ejecutar la función "sumar_vectores()"

# Muestra por pantalla los vectores previamente ingresados, y el vector resultante de invocar la función "sumar_vectores()"

print("El resultado de sumar las componentes de los vectores ("+str(primer_comp_de_u)+","+str(segunda_comp_de_u)+") y ("+str(primer_comp_de_v)+","+str(segunda_comp_de_v)+") es: {}".format(resultado))


'''
Ingreso de datos e invocación de la función multiplicar_escalar
'''

print('A continuación se ejecuta el algoritmo de multiplicar un vector por un escalar'+'\n')

print('Ingrese el valor de la primer componente del vector a')
prim_comp = float(input())

print('Ingrese el valor de la segunda componente del vector a')
seg_comp = float(input())

print('Ingrese el valor del escalar que multiplicará a las componentes del vector')
escalar = float(input())

res = multiplicar_escalar(escalar, prim_comp, seg_comp)

print('El vector resultante es: {}'.format(res))