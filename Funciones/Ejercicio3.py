'''Ejercicio 1

Crear una funcion que pida dos numeros. 
Si el primero es mayor al segundo, 
el programa debe retornar el valor 1; 
si el segundo es mayor al primero, debe retornar -1; 
si ambos son iguales, debe retornar 0
'''
def funcion1(val1, val2):

    if val1 == val2:
        return 0
    elif val1>val2:
        return 1
    else:
        return -1

numero1 = int(input("Ingrese el valor 1: "))
numero2 = int(input("Ingrese el valor 2: "))

print(funcion1(numero1,numero2))

