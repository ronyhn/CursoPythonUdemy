from math import sqrt
print("Bienvenido al programa para la formula cuadratica")
valorA = float(input("Ingrese el valor de a: "))
valorB = float(input("Ingrese el valor de b: "))
valorC = float(input("Ingrese el valor de c: "))
solucion1=0
solucion2=0

if(valorB**2 - 4*valorA*valorC) < 0:
    print("No hay solucion al ejercicio") 
else:
    solucion1 = (-valorB + sqrt(valorB**2 - 4 * valorA * valorC)) / (2 * valorA)
    solucion2 = (-valorB - sqrt(valorB**2 - 4 * valorA * valorC)) / (2 * valorA)
    print("La solucion es \nr1: ", str(solucion1), " ,", "\nr2: ", str(solucion2))