#Escribe un programa que pida dos palabras y diga si riman o no. 
#Si coinciden las tres últimas letras tiene que decir que riman. 
#Si coinciden sólo las dos últimas tiene que decir que riman un poco 
#y si no, que no riman.

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

finpalabra1 = palabra1[-3:]
finpalabra2 = palabra2[-3:]

if finpalabra1==finpalabra2:
    print("Las palabras {} y {} riman!!!!".format(palabra1,palabra2))
elif (finpalabra1[0]==finpalabra2[0] and finpalabra1[1] == finpalabra2[1]) or (finpalabra1[1] == finpalabra2[1] and finpalabra1[2] == finpalabra2[2] or (finpalabra1[0]==finpalabra2[0] and finpalabra1[2]==finpalabra2[2])):
    print("Las palabras {} y {} riman poco".format(palabra1,palabra2))
else:
    print("Las palabras {} y {} no riman".format(palabra1,palabra2))