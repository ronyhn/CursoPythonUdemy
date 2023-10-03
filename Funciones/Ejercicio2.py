''' Ejercicio 2
    Escribir una función que reciba un 
    número entero positivo y devuelva su factorial.
'''

valor = int(input("Ingrese el valor para calcular el factorial: "))
while (valor <0):
    print("El valor ingresado no es un entero positivo, intente de nuevo")
    valor = int(input("Ingrese el valor para calcular el factorial: "))

def factorial(numero):
    dato = 1
    for i in range(1,numero):
        dato *= i+1
    return dato

print(factorial(valor))