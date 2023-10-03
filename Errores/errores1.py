while True:
    try:
        num1 = int (input("Ingresa un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except KeyboardInterrupt:
        print("\n Has cancelado la ejecucion ")
    finally:
        print("Programa ejecutado con éxito")