# Script que utiliza el método format para darle formato a la salida del texto por consola

print("Ingrese su nombre")
nombre = input()

print("Ingrese su edad")
edad = int(input())

print("Su nombre es {0} y su edad es {1}".format(nombre, edad))

# Otra forma de utilizar el método format

print("Su nombre es {name} y su edad es {age}".format(name=nombre, age=edad))