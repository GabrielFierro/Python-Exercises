# Algoritmo que dados dos números realiza las operaciones de suma, resta, multiplicación y división entre ambos.

# Zona de inicialización de variables
numero = 0.0
otroNumero = 0.0
resultado = 0.0

print("Ingrese el valor de un número")
numero = int(input())

print("Ingrese el valor de otro número")
otroNumero = int(input())

# Se suman los valores ingresados por el usuario y se muestra por pantalla el resultado

resultado = numero + otroNumero

print("La suma entre los números " + str(numero) + " y " + str(otroNumero) + " es " + str(resultado))

# Se restan los valores ingresados por el usuario y se muestra por pantalla el resultado

resultado = numero - otroNumero

print("La resta entre los números " + str(numero) + " y " + str(otroNumero) + " es " + str(resultado))

# Se multiplican los valores ingresados por el usuario y se muestra por pantalla el resultado

resultado = numero * otroNumero

print("El producto entre los números " + str(numero) + " y " + str(otroNumero) + " es " + str(resultado))

# Se dividen los valores ingresados por el usuario y se muestra por pantalla el resultado en float

resultado = numero / otroNumero

print("La división con decimales entre los números " + str(numero) + " y " + str(otroNumero) + " es " + str(resultado))


# Se dividen los valores ingresados por el usuario y se muestra por pantalla el resultado en entero

resultado = numero // otroNumero

print("La división entera entre los números " + str(numero) + " y " + str(otroNumero) + " es " + str(resultado))
