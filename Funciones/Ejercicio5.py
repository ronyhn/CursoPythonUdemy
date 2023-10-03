'''Ejercicio 1
Crear un programa que tenga dos funciones, 
una que contenga el area de un cuadrado con argumentos de base y altura; 
y la otra el area de un circulo con argumento de radio
'''
import math
def areaRectangulo(base, altura):
    return base*altura

def areaCirculo(radio):
    return round(math.pi * math.pow(radio,2),2)

valorBase = float(input("Ingrese el valor de la base: "))
valorAltura = float(input("Ingrese el valor de la altura: "))
print("El area del rectrangulo es: {} metros cuadrados".format(areaRectangulo(valorBase,valorAltura)))

valorRadio = float(input("Ingrese el valor del radio: "))
print("El area del circulo es: {} metros cuadrados".format(areaCirculo(valorRadio)))
