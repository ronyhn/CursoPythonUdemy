'''Ejercicio 2
Escribir una función que reciba una muestra de números 
en una lista y devuelva su medida.
''' 
def medidaTupla(*num):
    return(len(num))

print(medidaTupla(2,4,5,6,7,8,10))