'''Ejercicio 1

Realizar un programa que conste de una 
clase llamada Estudiante, que tenga como 
atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no.'''

class Estudiante():
    def __init__(self,Nombre,Nota):
        self.Nombre = Nombre
        self.Nota = Nota

    def aprobado(self):
        if self.Nota >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

    def imprime(self):
        print("Hola, me llamo {}, y obtuve una nota de {}, por lo cual estoy {}".format(self.Nombre, self.Nota, self.aprobado()))

nombre = input("Ingrese el nombre del Estudiante: ")
nota = int(input("Ingrese la nota: "))

nino = Estudiante(nombre,nota)
nino.imprime()
