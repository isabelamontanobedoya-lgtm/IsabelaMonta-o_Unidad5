# Forma antigua
# f = open("datos.txt", "r")
# contenido = f.read()
# f.close()

# Forma moderna (recomendad)
# with open("datos.txt", "r") as f:
#     contenido = f.read()
#     f.name()
# Ya está cerrado automáticamente aquí

nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")

#Contexto de escritura
# Ejercicio: Leer todo el archivo en este mismo contexto
with open(nombre_archivo, "w+") as archivo:
    datos = input("Escribe tu primer secreto:")
    archivo.write(datos)
    archivo.seek(0) #Mover el puntero del archivo al inicio
    frase = archivo.read()
    print(frase)
