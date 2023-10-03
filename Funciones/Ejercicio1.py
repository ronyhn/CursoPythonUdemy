'''Ejercicio 1

Crear un programa que tenga una lista, 
luego crear una funcion con la cual se 
van a pedir numeros al usuario para agregar 
a la lista. Debes crear una segunda funcion 
en donde se ordenen los numeros pares e impares 
dentro de dos listas nuevas
'''

lista = [1,2,3,4,5,6,7]

def agregaNumeros(val):
    valor = 0
    valorNuevo = int(input("Ingrese el valor a agregar, ingresar -1 para salir: "))
    while (valorNuevo != -1):
        val.append(valorNuevo)
        valorNuevo = int(input("Ingrese el valor a agregar, ingresar -1 para salir: "))
    return val


print(agregaNumeros(lista))
print(lista)