#Algoritmo que crea una lista con elementos, la recorre y muestra por pantalla sus elementos

"""
There are four collection data types in the Python programming language:

    - List is a collection which is ordered and changeable. Allows duplicate members.
    - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    - Set is a collection which is unordered and unindexed. No duplicate members.
    - Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Changeable: Cambiante. # Unchangeable: Incambiante - inmutable
"""

lista = [1,2,3,4,5,6]

i = 0

while i < len(lista):
    print(lista[i])
    i+=1



