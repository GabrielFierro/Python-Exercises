# Algoritmo que le solicita al usuario que ingrese datos por teclado, los carga en una lista y luego mediante el bucle for recorre la lista y suma sus elementos, mostrando el resultado por consola

# Zona de inicialización de variables
lista = []
resultado = 0

print('Ingrese la cantidad de números que desea ingresar')
cant = int(input())

# Carga la estructura de tipo List
for i in range(cant):
    print('Ingrese un número para agregar a la lista')
    numero = int(input())

    lista.append(numero)

# Muestro por consola los elementos que posee la lista
print('Lista:',lista) 

# Suma los elementos de dicha estructura
for i in range(cant):
    resultado = resultado + lista[i] 

# Muestro por consola el resultado de sumar los elementos de la lista
print('Resultado:',resultado)