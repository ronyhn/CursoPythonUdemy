'''class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = FabricaTelefonos()
print(telefono.marca)

telefono.ElaborarHuawei()
print(telefono.marca)
'''
class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
        print("Estoy ejecutando el metodo Init, porque se ha ceado un nuevo objeto")

telefono = FabricaTelefonos("Apple", "Azul")
print(telefono.marca)
print(telefono.color)
