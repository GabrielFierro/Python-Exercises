# List is a collection which is ordered and changeable. Allows duplicate members.
# Una lista es una colección que está ordenada y es variable. Acepta elementos duplicados.

# Algoritmo que dada una lista cargada con elementos, muestra los elementos que se encuentran en una posición par.

lista = [0, "hola", 1, "mundo", 3, ", bienvenidos"]

i = 0

while i < len(lista):
    if i % 2 != 0:
        print(lista[i])
    i+=1