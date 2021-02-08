class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)


class Gato(Animal):
    tipo = "gato"

    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("Hola, soy un gato extendido!")


class Perro(Animal):
    tipo = "perro"

    def __init__(self, nombre, onomatopeya):
        # Hace referencia a la clase padre de Perro, es decir a la clase Animal
        super().__init__(nombre, onomatopeya)
        print("Instanciando un perro")


class Canario(Animal):
    tipo = "canario"


gato = Gato("Perla", "maullido")
gato.saludo()

perro = Perro("Fluffy", "ladrido")
perro.saludo()

canario = Canario("Piolin", "silbido")
canario.saludo()
