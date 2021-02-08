try:
    number = int(input("Ingrese un valor: "))
    number/0

except ValueError:
    # Excepción que muestra un cartel por consola cuando el valor ingresado no es numérico
    print("Error. No se puede dividir una cadena de caracteres")

except Exception as c:
    # Excepción que me muestra el tipo de error por consola
    print(type(c).__name__)
