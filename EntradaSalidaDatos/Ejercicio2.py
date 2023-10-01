print("Bienvenido al programa para obtener las notas de un estudiante")
p1=float(input("Ingrese la nota de la practica 1: "))
p2=float(input("Ingrese la nota de la practica 2: "))
p3=float(input("Ingrese la nota de la practica 3: "))
ep=float(input("Ingrese el valor del examen parcial: "))
ef=float(input("Ingrese el valor del examen final: "))
pp=(p1+p2+p3)/3
prom =(pp + 2*ep + 3*ef)/6
print("La nota final del alumno es ", str(prom))

