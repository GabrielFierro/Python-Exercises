# A Stack is a collection of objects that stores items in a Last-In, First-Out (LIFO) manner.
# We can only access to the top element of a stack. 

una_pila = [2,4,6,8,10]

# The operations can be implemented using the list methods such as append and pop.

una_pila.append(12) # With the method append, allow to stack the element 12

print('The elements of stack: ' , una_pila)

una_pila.pop()#return the removed element

print('The elements of stack: ' , una_pila)