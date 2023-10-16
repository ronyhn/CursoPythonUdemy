'''
Ejercicio 1
Crear un programa con tres clases 
Universidad, con atributos: Nombre (Donde se almacena el nombre de la Universidad), Otra llamada:
Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada:
Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
'''

class Universidad():
    def __init__(self, Univ):
        self.Univ = Univ
    
class Carrera():
    def __init__(self, Especialidad):
        self.Especialidad = Especialidad

class Estudiante():
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

class Persona(Universidad, Estudiante, Carrera):
    def __init__(self,Univ,Nombre, Edad, Especialidad):
        Universidad.__init__(self,Univ)
        Carrera.__init__(self, Especialidad)
        Estudiante.__init__(self, Nombre, Edad)
        
    def imprimePersona(self):
        print("El nombre del estudiante es: {}".format(self.Nombre))
        print("Con edad : {} años".format(self.Edad))
        print("Inscrito en la Universidad: {}".format(self.Univ))
        print("Cursando la especialidad de : {}".format(self.Especialidad))

persona = Persona("UNAH","Alejandra Nuñez",39,"Ingenieria en Sistemas")
persona.imprimePersona()