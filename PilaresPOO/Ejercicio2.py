'''Ejercicio 1

Realizar un programa en el cual se declaren dos valores 
enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.'''

class Calculadora():
    def __init__(self,Valor1,Valor2):
        self.Valor1 = Valor1
        self.Valor2 = Valor2
    
    def Suma(self):
        return self.Valor1 + self.Valor2
    
    def Resta(self):
        return self.Valor1 - self.Valor2
    
    def Multiplicacion(self):
        return self.Valor1 * self.Valor2
    
    def Division(self):
        return self.Valor1 / self.Valor2
    
valor1 = float(input("Ingrese el valor 1: "))
valor2 = float(input("Ingrese el valor 2: "))

calqui = Calculadora(valor1,valor2)

print("El valor calculadora de los numero {} y {} son: De la suma es {}, resta {}, multiplicacion {}, division {}".format(calqui.Valor1, calqui.Valor2, calqui.Suma(), calqui.Resta(), calqui.Multiplicacion(), calqui.Division()))
