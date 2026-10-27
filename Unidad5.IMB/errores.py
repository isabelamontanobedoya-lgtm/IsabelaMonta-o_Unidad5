try:
    numero = int(input("Ingrese un número entero: "))
except ValueError:
    print("El dato ingresado es incorrecto.")
else:
    print(numero)
finally:
    print("Fin de esta parte")
    