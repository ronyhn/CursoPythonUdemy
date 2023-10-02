'''Ejercicio 2
Pedir al usuario que ingrese 2 numeros, después, 
se debe mostrar el rango de esos 2 números, pero, 
solo imprimiendo los números que sean impares
'''

inicio = int(input("Ingrese el valor inicial: "))
final = int(input("Ingrese el valor final: "))
if final < inicio:
    print("El valor final es mayor al valor inicial, intente de nuevo!")
else:
    for i in range(inicio,final+1):
        if i%2 == 0:
            print(i)
