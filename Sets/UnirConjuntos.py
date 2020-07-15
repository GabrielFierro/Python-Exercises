# Algoritmo que une dos conjuntos de elementos mediante el método union().

animals1 = {"cow", "tiger", "bear", "monkey", "squirrel", "fox", "raccoon"}
animals2 = {"dog", "kangaroo", "koala bear", "panda", "zebra"}

animals3 = animals1.union(animals2) 
# El método union() excluye los elementos duplicados y no establece un orden sobre el nuevo conjunto.

print(animals3)