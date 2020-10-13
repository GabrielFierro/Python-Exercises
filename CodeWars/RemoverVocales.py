# Algoritmo que dada unca cadena de caracteres que el usuario ingresa, invoca a la funcion remover_vocales.

def remover_vocales(cadena):
    
    # Función que dada una cadena de caracteres, verifica si posee vocales y, en caso afirmativo las elimina de dicha cadena, retornando una nueva cadena sin vocales.
    
    # Zona de inicialización de variable
    res = ''

    for i in range(0,len(cadena)):
        
        # Recorre la cadena buscando vocales, si las encuentra las reemplaza por una cadena vacía

        if cadena[i] == 'a':
            res = res + ''
        elif cadena[i] == 'A':
            res = res + ''
        elif cadena[i] == 'e':
            res = res + ''
        elif cadena[i] == 'E':
            res = res + ''
        elif cadena[i] == 'i':
            res = res + ''
        elif cadena[i] == 'I':
            res = res + ''
        elif cadena[i] == 'o':
            res = res + ''
        elif cadena[i] == 'O':
            res = res + ''
        elif cadena[i] == 'u':
            res = res + ''
        elif cadena[i] == 'U':
            res = res + ''
        else:
            res = res + cadena[i]
        
    return res


# Ingreso de datos por parte del usuario

print('Ingrese una cadena de caracteres de la que desea sacar sus vocales')

palabra = input()

resultado = remover_vocales(palabra)

print('La palabra ingresada',palabra,'sin caracteres resulta',resultado)