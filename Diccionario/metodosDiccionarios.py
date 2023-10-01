diccionario = {1: 2, 2:3, 3:4}
diccionario.pop(3)
print(diccionario)
print(diccionario.get(2))

diccionario.setdefault(4 ,5)
print(diccionario)

diccionario2 = {4 : 5, 6 : 7}
diccionario.update(diccionario2)
print(diccionario)

diccionario.copy()