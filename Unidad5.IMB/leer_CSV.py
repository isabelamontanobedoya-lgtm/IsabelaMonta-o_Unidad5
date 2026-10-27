import csv

with open("notas.csv", "r") as csvfile:
    print(csvfile)
    lector = csv.reader(csvfile, delimiter=";")
    print(lector)
    encabezado = next
    for dato in lector:
        print(dato)
