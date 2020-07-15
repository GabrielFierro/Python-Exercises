# Algoritmo que dada una estructura de tipo set cargada con elementos de tipo 'str', recorre el conjunto mediante la estructura for y muestra todos sus elementos.

fruits = {"apple", "banana", "cherry", "orange", "watermelon", "pear"}

# Los conjuntos no tienen índice, por lo que para acceder a sus elementos puedo usar la estructura for.
# "in" es una palabra reservada denominada "keyword", que pregunta si un valor específico se encuentra en el conjunto.

for x in fruits: 
    print(x)
