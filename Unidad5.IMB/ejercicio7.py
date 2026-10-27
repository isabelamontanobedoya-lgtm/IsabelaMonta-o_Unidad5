# Abrir un archivo usando el modo x

with open("datos.txt", "x+") as file:
    texto = file.read()
    print(texto) 
# Si el archivo ya existe, este generara un error porque el modo x es solo para lectura, no deja sobre-escribir dentro de un archivo, o sea solo es para un archivo nuevo
