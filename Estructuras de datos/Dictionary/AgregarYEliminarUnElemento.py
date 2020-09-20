# Algoritmo que dado un diccionario inicializado, agrega un elemento y lo muestra por consola. Luego, procede a removerlo mediante el método pop()

diccionario = {
    "Nombre": "Rocco",
    "Raza": "Bulldog",
    "Fecha de nacimiento": "07/10/2018"
}

diccionario["color"] = "marrón" # Agrega la clave "color" y el valor "marrón" al diccionario

print(diccionario)  # Muestra por consola los valores actuales del diccionario

diccionario.pop("color")    # Remueve del diccionario aquel elemento que posee como clave a "color"

print(diccionario)  # Muestra por consola los valores actuales del diccionario

# Además, se puede remover el último elemento insertado mediante el método popitem()
# Para ello, agrego una clave junto a un valor, para luego removerlos mediante dicho método

diccionario["collar"] = "no"    

print(diccionario)  # Muestra por consola los valores actuales del diccionario

diccionario.popitem()

print(diccionario)  # Muestra por consola los valores actuales del diccionario

# También, se puede utilizar la palabra clave "del" para eliminar un elemento del diccionario a partir de la clave
# Nuevamente agrego una clave nueva junto a un valor, para luego removerlos utilizando la clave "del"

diccionario["collar"] = "si"

print(diccionario)  # Muestra por consola los valores actuales del diccionario

del diccionario["collar"]

print(diccionario)  # Muestra por consola los valores actuales del diccionario 