# Algoritmo que recibe una cantidad de minutos ingresada por el usuario, y muestra por consola el equivalente en hora/s y minuto/s.

# Zona de inicialización de variables
minuto = 0
unaHora = 0
unMinuto = 0

print("Ingrese los minutos que desea convertir a hora/s y minuto/s")
minuto = int(input())

unaHora = minuto//60

unMinuto = minuto//unaHora

print("Los minutos " + str(minuto) + " son " + str(unaHora) + " horas y " + str(unMinuto) + " minutos")

