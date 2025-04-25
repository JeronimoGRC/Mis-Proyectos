import json

# Métodos más utilizados de la biblioteca json:

# 1. json.dumps(obj):
# Convierte un objeto Python a una cadena JSON.
data = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
data_json = json.dumps(data)
print("\nJSON generado:")
print(data_json)

# 2. json.loads(json_str):
# Convierte una cadena JSON a un objeto Python.
data_python = json.loads(data_json)
print("\nJSON convertido a diccionario Python:")
print(data_python)

# 3. Escritura de un archivo JSON
# Guarda un objeto Python en un archivo JSON.
with open("archivo.json", "w") as file:
    json.dump(data, file)
print("\nArchivo JSON guardado correctamente.")

# 4. Lectura de un archivo JSON
# Carga datos desde un archivo JSON a un objeto Python.
with open("archivo.json", "r") as file:
    data_cargado = json.load(file)
print("\nDatos cargados desde el archivo JSON:")
print(data_cargado)

# 5. json.dumps() con indentación
# Convierte un objeto Python a una cadena JSON con formato legible.
data_json_indent = json.dumps(data, indent=4)
print("\nJSON formateado con indentación:")
print(data_json_indent)

# 6. json.dump() con indentación en archivo
# Guarda un objeto Python en un archivo JSON con formato legible.
with open("archivo_indent.json", "w") as file:
    json.dump(data, file, indent=4)
print("\nArchivo JSON con indentación guardado correctamente.")

# 7. Manejo de listas en JSON
# Convierte una lista de diccionarios en JSON.
lista_datos = [
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Luis", "edad": 22}
]
lista_json = json.dumps(lista_datos)
print("\nLista de diccionarios convertida a JSON:")
print(lista_json)

# 8. Cargar JSON desde un string con encoding
# Decodificar JSON con encoding específico.
data_encoded = json.loads(data_json.encode("utf-8"))
print("\nJSON decodificado con encoding UTF-8:")
print(data_encoded)
