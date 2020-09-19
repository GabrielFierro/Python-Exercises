# Una pila es una colección de objetos que almacena ítems de la forma "Last-in", "First-Out". 
# Es decir, que solo podemos acceder a un elemento por el frente de la pila. 

"Zona de declaración e inicialización de variable"

una_pila = [2,4,6,8,10]

# las operaciones pueden ser implementadas utilizando los métodos de la lista, tales como append() y pop()

# Con el método append(), se almacena el elemento 0, 12 y -1 en la pila respectivamente.
una_pila.append(0) 
una_pila.append(12) 
una_pila.append(-1)

print('Se muestra la estructura de tipo Stack:',una_pila)

print('Elementos eliminados mediante el método pop():')

print(una_pila.pop()) # Elimina el elemento del tope de la pila
print(una_pila.pop()) # Elimina el elemento del tope de la pila
print(una_pila.pop()) # Elimina el elemento del tope de la pila

print('Se muestra la estructura de tipo Stack:',una_pila)