'''
Todas las clases tienen una función llamada __init__(), la cual siempre se está ejecutando cuando la clase ha sido iniciada.
La función __init__() se utiliza para asignar valores a las propiedades de los objetos, u otras operaciones que son necesarias para cuando el objeto está siendo creado.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

p1 = Person("Amy",23)

print(p1.name)
print(p1.age)