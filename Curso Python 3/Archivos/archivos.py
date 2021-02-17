import os

# El párametro 'r' (read) viene por defecto
# c = open('nombres.txt', 'r')

# El parámetro 'a' (append) me sirve para modificar el archivo, agregando al final del mismo texto.
# c = open('nombres.txt', 'a')

# El parámetro 'w' (write) va a abrir el archivo existente, y en caso de no existir, simplemente crea un nuevo archivo con el nombre dado
# c = open('nombres.txt', 'a')

# Con el parámetro 'x' yo indico que quiero crear un nuevo archivo, en caso de que el archivo con el nombre indicado ya exista, vamos a obtener un error
# c = open('nombres.txt', 'a')


''' Segunda parte '''


c = open('nombres.txt')
# Con el método readline() le indico que quiero leer una a una, las líneas de mi archivo
# print(c.readline())

# Para tener un control diferente sobre cada una de las lineas de texto de mi archivo utilizo la estructura for (si quiero iterar sobre todas)
# for x in c:
#    print(x)

c.close()  # Método que cierra el archivo

file = open('archivo_vacio.txt', 'a')

file.write('Agregaremos una nueva linea a nuestro archivo\n')

file.close()

x = open('archivo_vacio.txt')

print(x.read())


# Eliminando archivos

if os.path.exists('prueba.txt'):
    os.remove('prueba.txt')
else:
    print('El archivo no existe')
