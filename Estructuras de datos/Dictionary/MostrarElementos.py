# Algoritmo que inicializa una variable de tipo Dictionary y la carga con claves y valores. Luego, recorre toda la estructura y muestra el resultado por consola.

diccionario = {
    "Año": "2020",
    "Mes": "Julio",
    "Dia": "Miércoles 15"
}

# Recorre toda la estructura y muestra por consola todos los nombres claves
for x in diccionario:
    print(x)

# Recorre toda la estructura y muestra por consola todos los valores
for x in diccionario:
    print(diccionario[x])

# Recorre toda la estructura y muestra por consola todos los valores mediante el método values()
for x in diccionario.values():
    print(x)

# Recorre toda la estructura y muestra por consola todos los nombres claves junto a sus valores mediante el método items()
for x,y in diccionario.items():
    print(x,y)