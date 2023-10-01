diccionario = {'Guatemala' : "Ciudad de Guatemala" , "El Salvador" : "San Salvador", 'Honduras': "Tegucigalpa", 'Nicaragua' : "Managua",'Costa Rica': "San Jose", 'Panama' : "Panama", 'Argentina': "Buenos Aires", 'Colombia':"Bogota", 'Venezuela' : "Caracas", 'Espania' : "Madrid"}
pais = input("Ingrese el Pais a Consultar: ")
pais = pais.title()
if pais not in diccionario.keys():
    print("El pais buscado no existe, intente de nuevo")
else:
    print("La capital es : ", diccionario[pais])