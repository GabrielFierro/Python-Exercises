'''
Todas las clases tienen una función llamada __init__().
La función __init__() se utiliza para asignar valores a las propiedades de los objetos, u otras operaciones que son necesarias para cuando el objeto está siendo creado.
El parámetro self hace referencia a la instancia actual sobre la que se está trabajando, y se utiliza para acceder a los atributos que pertenecen a la clase.
'''

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("Ingrese el nombre de una persona")
nombre = input()

print("Ingrese la edad de una persona")
edad = int(input())

mi_persona = Persona(nombre, edad) # Crea un objeto de tipo Persona

print("\n""El nombre de la persona es:",mi_persona.name) 
print("La edad de la persona es:",mi_persona.age)