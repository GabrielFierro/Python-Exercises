"Zona de declaración e inicialización de variable"
my_list = []

# Método append(): Agrega un elemento al final de la lista.

my_list.append('red')
my_list.append('green')
my_list.append('blue')

print(my_list)

# Método pop(): Remueve el último elemento de la lista.

my_list.pop() 

print(my_list)

# Método remove: Remueve el primer elemento de la lista, con un valor especificado.

my_list.remove('green')

print(my_list)

# Método clear(): Remueve todos los elementos de la lista.

my_list.clear()

print(my_list)

# Método append(): Agrega un elemento al final de la lista.

my_list.append('red')
my_list.append('green')
my_list.append('blue')

# Método copy(): Copia los elementos de una lista dada, en otra nueva.

new_list = []

new_list = my_list.copy()

print(my_list)
print(new_list)