'''Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, 
pedir al usuario dos numeros y mostrar el rango de numeros 
entre ambas cifras '''

for i in range(0,10):
    print(i+1)
valor1 = int(input("Ingrese el valor inicial: "))
valor2 = int(input("Ingrese el valor final: "))

if valor1 <0 or valor2 >10:
    print("Los valores proporcionados son incorrecto, intente de nuevo")
else:
    for i in range(valor1-1,valor2):
        print(i+1)

             