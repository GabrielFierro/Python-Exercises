#Algoritmo que le solicita al usuario el nombre y apellido, y muestra por consola las iniciales de cada string mencionado.

# Zona de inicialización de variables
nombre = ""
apellido = ""
inicialNombre = ""
inicialApellido = ""

print("Ingrese su nombre")
nombre = input()

print("Ingrese su apellido")
apellido = input()

inicialNombre = nombre[0]

inicialApellido = apellido[0]

print("La inicial del nombre " + nombre + " es " + inicialNombre + " y la inicial del apellido es " + inicialApellido)
