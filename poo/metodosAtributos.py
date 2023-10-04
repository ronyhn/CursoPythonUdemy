class FabricaTelefonos():
    marca = "Apple"
    color = "Azul"
    memoriaRam = 16
    storage = 64
    def llamar(self, mensaje):
        return mensaje
    def escucharMusica(self):
        print("Estas escuchando musica")

telefono = FabricaTelefonos()
print(telefono.marca)
print(telefono.color)
print(telefono.memoriaRam)
print(telefono.storage)
print(telefono.llamar("Hola, Con quien hablo"))
telefono.escucharMusica()