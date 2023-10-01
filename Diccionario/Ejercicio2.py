diccionario ={1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta",7 : "Villa"}
print("Ingrese el numero del jugador: ")
numero = int(input())
if numero not in diccionario.keys():
    print("El numero del jugador que esta buscando no existe, intente de nuevo")
else:
    print("El jugador es: ", diccionario[numero])
