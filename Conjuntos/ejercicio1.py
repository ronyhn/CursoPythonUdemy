'''Ejercicio 1
Escribir una tupla con los meses del año, 
luego, pide al usuario un numero, el que haya 
ingresado, es el mes que debe mostrar en la tupla'''

tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mesElegido = int(input("Ingrese el numero que quiere ver: "))
if mesElegido not in range(0,11):
    print("Opcion elegida no valida")
else:
    print(tupla[mesElegido])