'''Ejercicio 2
Escribir una función que calcule el total de una 
factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y 
el porcentaje de IVA a aplicar, y 
devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.'''

def calcTotal(precio, ISV):
    if ISV == 0:
        return precio * 0.21 + precio
    else:
        return precio * ISV + precio

monto = float(input("Ingrese el valor del articulo: "))
Impuesto = float(input("Ingrese el porcentaje de impuesto: "))

print("El total a pagar con impuesto es: ", calcTotal(monto,Impuesto))
