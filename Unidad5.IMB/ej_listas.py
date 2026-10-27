aviones = ["Boeing 787", "Airbus A320", " Cirrus SR22"]

file = open("aviones.text", "w")

for avion in aviones:
  file.write(avion + "\n")

file.close()