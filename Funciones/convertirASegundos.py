def convertir_tiempo (cant_horas, cant_minutos, cant_segundos):

    # Algoritmo que dado un tiempo en horas, minutos y segundos, calcula el tiempo en segundos y retorna el resultado.

    hora_a_segundos = (cant_horas * 60) * 60

    minuto_a_segundos = cant_minutos * 60

    resultado = hora_a_segundos + minuto_a_segundos + cant_segundos

    return resultado


print('Ingrese el tiempo en horas que desea convertir')
tiempo_h = int(input())

print('Ingrese el tiempo en minutos que desea convertir')
tiempo_m = int(input())

print('Ingrese el tiempo en segundos que desea convertir')
tiempo_s = int(input())

resultado = convertir_tiempo(tiempo_h,tiempo_m,tiempo_s)

print('El resultado es:',resultado)