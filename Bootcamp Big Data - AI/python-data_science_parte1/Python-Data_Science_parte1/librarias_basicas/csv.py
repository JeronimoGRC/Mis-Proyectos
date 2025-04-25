import csv

# Métodos más utilizados de la biblioteca csv:

# 1. Escritura de un archivo CSV
# Escribe una lista de filas en un archivo CSV
with open("archivo.csv", mode="w", newline="") as file: #Abre un archivo con el modo de writer
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad", "Ciudad"])
    writer.writerow(["Ana", 25, "Madrid"])
    writer.writerow(["Carlos", 30, "Barcelona"])
    writer.writerow(["Luis", 22, "Valencia"])
print("\nArchivo CSV creado y escrito correctamente.")

# 2. Lectura de un archivo CSV
# Lee un archivo CSV y muestra su contenido
with open("archivo.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 3. Escritura de un archivo CSV con diccionarios
# Escribe un archivo CSV utilizando diccionarios
with open("archivo_dict.csv", mode="w", newline="") as file:
    fieldnames = ["Nombre", "Edad", "Ciudad"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Nombre": "Ana", "Edad": 25, "Ciudad": "Madrid"})
    writer.writerow({"Nombre": "Carlos", "Edad": 30, "Ciudad": "Barcelona"})
    writer.writerow({"Nombre": "Luis", "Edad": 22, "Ciudad": "Valencia"})
print("\nArchivo CSV con diccionarios creado correctamente.")

# 4. Lectura de un archivo CSV con diccionarios
# Lee un archivo CSV utilizando diccionarios
with open("archivo_dict.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))

# 5. Añadir datos a un archivo CSV existente
# Agrega filas a un archivo CSV sin sobrescribir su contenido
with open("archivo.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Laura", 27, "Sevilla"])
print("\nFila añadida correctamente al archivo CSV.")

# 6. Manejo de delimitadores personalizados
# Escribe un archivo CSV con delimitador personalizado
with open("archivo_delimitador.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Nombre", "Edad", "Ciudad"])
    writer.writerow(["Ana", 25, "Madrid"])
print("\nArchivo CSV con delimitador personalizado creado correctamente.")

