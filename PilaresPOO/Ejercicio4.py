'''Ejercicio 1

Crear una clase llamada Marino(), 
con un metodo que sea hablar, 
en donde muestre un mensaje que diga "Hola...". Luego, 
crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar 
por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, 
pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro'''

class Marino():
    def hablar(self):
        print("Hola...")
    
class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")
    
class Foca(Marino):
    def __init__(self,mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)
        
mari = Marino()
mari.hablar()

pulpito = Pulpo()
pulpito.hablar()

foca = Foca("Hola soy la foca")
foca.hablar()