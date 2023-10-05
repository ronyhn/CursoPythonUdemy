class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0

    @property
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador
a=A()
print(a.cuenta)
print(a.contador)

''' def incrementar(self):
        self._contador +=1
    
    def cuenta(self):
        return self._contador
    
a=A()'''