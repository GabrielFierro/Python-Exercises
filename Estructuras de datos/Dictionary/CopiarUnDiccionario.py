# Algoritmo que dado un diccionario inicializado, muestra por consola sus valores actuales y luego, realiza una copia del diccionario actual en otro y muestra ambos por consola

diccionario = {
    "pen": "blue",
    "pencil": "red", 
    "eraser": "white"
}

print(diccionario)  # Muestra por consola los valores actuales del diccionario 

nuevo_diccionario = diccionario.copy()

print("Diccionario original",diccionario)  # Muestra por consola los valores del diccionario original
print("Copia del diccionario original",nuevo_diccionario)    # Muestra por consola los valores de la copia del diccionario original

# Además, se puede realizar una copia del diccionario utilizando la función incorporada dict()

mi_diccionario = dict(diccionario) 

print("\nDiccionario original",diccionario)  # Muestra por consola los valores del diccionario original
print("Copia del diccionario original",mi_diccionario)    # Muestra por consola los valores de la copia del diccionario original