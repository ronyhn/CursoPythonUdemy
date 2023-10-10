class Animales():
    def __init__(self,nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self,nombre,sonido):
        super().__init__(nombre)
        self.sonido = sonido

class Gato(Perro):
    def __init__(self,nombre,sonido,ronronea):
        super().__init__(nombre,sonido)
        self.ronronea = ronronea

class Canario(Animales):
    def __init__(self,nombre,color):
        super().__init__(nombre)
        self.color = color

perro = Perro("Firulais", "Guaaaaaaaooo!")
print(perro.nombre)
print(perro.sonido)

gatito = Gato("RadioMichi","miauuuu",True)
print(gatito.nombre)
print(gatito.sonido)
print(gatito.ronronea)

canario = Canario("Piolin","Amarillo")
print(canario.nombre)
print(canario.color)

