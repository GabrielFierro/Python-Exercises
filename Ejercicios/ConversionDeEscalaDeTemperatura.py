# Algoritmo que convierte un valor dado de grados Fahrenheit a grados Celsius y muestra el resultado por consola.

print("Ingrese un valor en grados Fahrenheit")
gradoFahrenheit =  float(input())

gradoCelsius = (gradoFahrenheit-32)*5/9

print("El valor en grados Fahrenheit se expresa en Celsius como " + str(gradoCelsius)) 
