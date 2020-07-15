# Algoritmo que convierte un valor dado de grados Fahrenheit a grados Celsius y muestra el resultado por consola

# Zona de inicialización de variables
gradoFahrenheit = 0.0
conversion = 0.0

print("Ingrese un valor en grados Fahrenheit")
gradoFahrenheit =  float(input())

conversion = (gradoFahrenheit-32)*5/9

print("El valor en grados Fahrenheit se expresa en Celsius como " + str(conversion)) 
