'''
Clase llamada Usuario que define un método __init__, el cual se ejecutará siempre que se 
cree una instancia de la misma, la cual le asigna al objeto usuario, un nombre y un apellido
recibidos por parámetro.
'''


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        # Método que muestra por consola un saludo a la instancia que invoca éste método
        print("Hola, mi nombre es:", self.nombre, self.apellido)


class Admin(Usuario):
    # Clase que hereda de Usuario sus Atributos y Métodos
    def superSaludo(self):
        print("Hola, me llamo", self.nombre, "y soy Administrador")


    # Creación de un objeto de tipo Usuario con los valores "Gabriel" y "Fierro"
usuario = Usuario("Gabriel", "Fierro")

# Se muestar por consola el nombre y apellido del usuario
print(usuario.nombre, usuario.apellido)

# Invocación del método saludo perteneciente a la clase Usuario
usuario.saludo()
usuario.nombre = "Esteban"  # Se cambia el atributo de la propiedad nombre
usuario.saludo()

# # Se elimina la propiedad nombre del usuario, con la palabra reservada del
# del usuario.nombre
# # Muestra un error dado que la propiedad nombre no existe en la clase Usuario
# usuario.saludo()

# # Se elimina un usuario por completo, utilizando la palabra reservada del
# del usuario
# print(usuario)

admin = Admin("Super", "Administrador")

print(admin.nombre, admin.apellido)
admin.saludo()
admin.superSaludo()

# No se puede llamar a los métodos de las clases hijos porque el padre no las conoce
usuario.superSaludo()
