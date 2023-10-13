class Animales():
    def __init__ (self,mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago guau")

class Gato(Animales):
    def hablar(self):
        print("Yo soy un gatito que no habla")

perro = Perro("Guau")
perro.hablar()

animal = Animales("miau")
animal.hablar()

gatito =Gato("Nada")
gatito.hablar()