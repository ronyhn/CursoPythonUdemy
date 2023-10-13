'''Ejercicio 1

Crear una clase Fabrica que tenga los atributos de Llantas, 
Color y Precio; luego crear dos clases mas que hereden de Fabrica, 
las cuales son Moto y Carro. Crear metodos que muestren la cantidad 
de llantas, color y precio de ambos transportes. Por ultimo, 
crear objetos para cada clase y mostrar por pantalla los atributos de cada uno'''

class Fabrica():
    def __init__(self,Llantas,Color,Precio):
        self.Llantas = Llantas
        self.Color = Color
        self.Precio = Precio
    
    def imprimir(self):
        print("Los Atributos de este objeto son: Llantas -> {}, Color -> {}, Precio -> {}".format(self.Llantas, self.Color, self.Precio))

class Moto(Fabrica):
    pass

class Carro(Fabrica):
    pass

motito = Moto(2,"Azul", 25000)
motito.imprimir()

carrito = Carro(4,"Negro", 170000)
carrito.imprimir()