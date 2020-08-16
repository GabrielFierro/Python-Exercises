# Algoritmo que inicializa una variable de tipo Dictionary y la carga con claves y valores. Luego, verifica que la estructura posea la clave "Nombre" y muestra el resultado por consola.

diccionario = {
    "Nombre": "Rocco",
    "Raza": "Bulldog",
    "Fecha de nacimiento": "07/10/2018"
}

if "nombre" in diccionario:
    print("La clave nombre se encuentra en el diccionario")
else:
    print("La clave nombre no se encuentra en el diccionario")