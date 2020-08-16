# Algoritmo que inicializa una variable de tipo Dictionary y la carga con claves y valores. Luego, dada una clave le cambia su valor y muestra el resultado por consola.

diccionario = {
    "Año": "2020",
    "Mes": "Julio",
    "Dia": "Miércoles 15"
}

print(diccionario,'\n') # Se muestra el diccionario original

diccionario["Año"] = "2019"

print(diccionario) # Se muestra el diccionario actualizado