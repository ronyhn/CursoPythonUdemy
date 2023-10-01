'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre 
los valores al usuario, a su vez, debe pedir dos datos y 
esos que sean ingresados deben ser sustituidos en el primer 
y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]

print(lista)

dato1 = int(input("Ingrese un dato: "))

dato2 = int(input("Ingrese otro dato: "))

lista[0] = dato1
lista[1] = dato2

print(lista)