from collections import deque
# Algoritmo que dada una estructura de datos de tipo Cola cargada con elementos, recorre la estructura y muestra sus elementos
# A diferencia de la estructura de tipo Stack, se puede acceder tanto al frente como al final de tal estructura

"Zona de declaración e inicialización de variable"

my_queue = deque(['red','blue','yellow','brown','green'])

for x in my_queue:
    print(x)

# Accediendo al frente de la estructura
print('El elemento del frente es:',my_queue.popleft())

# Muestro los valores actuales
print('Los valores actuales son:',my_queue)

# Accediendo al final de la estructura
print('El elemento del final de la estructura es:',my_queue.pop())

# Muestro los valores actuales
print('Los valores actuales son:',my_queue)