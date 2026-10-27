# Código propenso a errores (Si el usuario escribe algo mal, el programa explota)
nombre = input("Dime qué archivo quieres leer: ")

# TODO: Añade el bloque try - except aquí
with open(nombre, "r") as archivo:
    print(archivo.read())

print("Fin del programa. Gracias por usar nuestro sistema.")