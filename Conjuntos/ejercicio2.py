'''Ejercicio 2
Escribir una tupla que tenga las letras del alfabeto. 
Luego, debes pedir al usuario un número, el que haya ingresado, 
es la letra que debe imprimir el programa'''

tupla = ('a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z')

opcion = int(input("Ingrese la letra que quiere ver: "))
if opcion not in range(0,26):
    print("Error, ha elegido una opcion incorrecta")
else:
    print(tupla[opcion])