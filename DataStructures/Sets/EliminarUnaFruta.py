# Algoritmo que remueve un elemento del conjunto mediante el método remove()

"Zona de declaración e inicialización de variable"

colors = {"yellow", "blue", "green", "brown", "violet", "purple"}

colors.remove("aple")

"""
Si la palabra pasada por parámetro no se encuentra, el método remove() muestra un error

Para sanar el error utilizo el método discard()

colors.discard("easy")
"""

print(colors)   