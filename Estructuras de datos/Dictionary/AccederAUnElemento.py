# Algoritmo que inicializa una variable de tipo Dictionary y la carga con claves y valores para luego mostrarlo por consola.

diccionario = {
    "Año": "2020",
    "Mes": "Julio",
    "Dia": "Miércoles 15"
}

# Para acceder a un elemento del diccionario se debe acceder con su nombre clave, dentro de los corchetes.

elemento = diccionario["Año"]

print(elemento,"\n")

# Puede resolverse utilizando el método get() de la siguiente forma

elemento = diccionario.get("Año")

print(elemento)