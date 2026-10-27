lista = ["El fin de la eternidad", "La biblia", "Sapiens", "Cadaver exquisito"]
lista2 = []

lista3 = [123, "hola", 34.5, "programacion"]
lista4 = []

for libro in lista:
     lista2.append(libro + "\n")

archivo = open("libros.txt", "a")
archivo.writelines(lista2)
archivo.close()
file = open("datos.txt", "w")

for dato in lista3:
    lista4.append(str(dato) + "\n")

file.close()
