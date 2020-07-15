# Algoritmo que une dos conjuntos de elementos mediante el método update().

animals1 = {"cow", "tiger", "bear", "monkey", "squirrel", "fox", "raccoon"}
animals2 = {"dog", "kangaroo", "koala bear", "panda", "zebra"}

animals1.update(animals2) 
# El método update() excluye los elementos duplicados y no establece un orden sobre el nuevo conjunto.
# Agrega los elementos del conjunto fruits2 al conjunto fruits1.

print(animals1)