# Algoritmo que determina la calificación final, teniendo en cuenta 3 evaluaciones parciales, el examen final y un trabajo final. Muestra el resultado por consola.

# Zona de inicialización de variables 
primerParcial = 0.0
segundoParcial = 0.0
tercerParcial = 0.0
examenFinal = 0.0
trabajoFinal = 0.0
calificacionFinal = 0.0
promedioParciales = 0.0
promedioExamenFinal = 0.0
promedioTrabajoFinal = 0.0

print("Ingrese la nota obtenida en el primer parcial")
primerParcial = float(input())

print("Ingrese la nota obtenida en el segundo parcial")
segundoParcial = float(input())

print("Ingrese la nota obtenida en el tercer parcial")
tercerParcial = float(input())

print("Ingrese la nota obtenida en el examen final")
examenFinal = float(input())

print("Ingrese la nota obtenida en el trabajo final")
trabajoFinal = float(input())

promedioParciales = (primerParcial + segundoParcial + tercerParcial) * 0.55 # Determina el 55% del promedio de sus tres calificaciones parciales

promedioExamenFinal = examenFinal * 0.3 # Determina el promedio del 30% con respecto al examen final

promedioTrabajoFinal = trabajoFinal * 0.15 # Determina un promedio de 15% con respecto al trabajo final

calificacionFinal = (promedioParciales + promedioExamenFinal + promedioTrabajoFinal)/3

print("La calificación final de la materia algoritmos es: " + str(calificacionFinal))
