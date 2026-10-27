file = open("texto_ejemplo.txt", "r", encoding="utf-8")

#read() leo el numero de caracteres indicados
# texto_leido = file.read(10)
# si read() no tiene parámetro, se lee todo el archivo
# readline() lee hasta que encuentra un "\n"

#readlines() lee el archivo en una lista, cada elemento es una linea
datos = file.readlines()

print(datos[0])

file.close()