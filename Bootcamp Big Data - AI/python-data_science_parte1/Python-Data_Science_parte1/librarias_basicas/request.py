import requests

# Métodos más utilizados de la biblioteca requests:

# 1. requests.get(url):
# Realiza una solicitud HTTP GET a la URL especificada.
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print("Respuesta GET:")
print(response.json())

# 2. requests.post(url, data/dict):
# Envía datos a un servidor a través de una solicitud POST.
data = {"title": "foo", "body": "bar", "userId": 1}
response_post = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=data)
print("\nRespuesta POST:")
print(response_post.json())

# 3. requests.put(url, data/dict):
# Actualiza un recurso en el servidor con una solicitud PUT.
data_update = {"title": "updated title"}
response_put = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1", json=data_update)
print("\nRespuesta PUT:")
print(response_put.json())

# 4. requests.delete(url):
# Elimina un recurso en el servidor con una solicitud DELETE.
response_delete = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1")
print("\nRespuesta DELETE:")
print(response_delete.status_code)

# 5. response.status_code:
# Devuelve el código de estado HTTP de la respuesta.
print("\nCódigo de estado de la respuesta GET:")
print(response.status_code)

# 6. response.headers:
# Devuelve los encabezados de la respuesta HTTP.
print("\nEncabezados de la respuesta GET:")
print(response.headers)

# 7. response.text:
# Devuelve el contenido de la respuesta como una cadena de texto.
print("\nContenido de la respuesta GET:")
print(response.text)

# 8. response.json():
# Devuelve la respuesta en formato JSON si es posible.
print("\nRespuesta GET en JSON:")
print(response.json())

# 9. requests.head(url):
# Realiza una solicitud HEAD para obtener los encabezados de una URL sin el cuerpo de la respuesta.
response_head = requests.head(url)
print("\nEncabezados de la respuesta HEAD:")
print(response_head.headers)

# 10. requests.options(url):
# Obtiene los métodos HTTP permitidos para un recurso específico.
response_options = requests.options(url)
print("\nMétodos permitidos:")
print(response_options.headers.get('Allow'))

# 11. requests.request(method, url, **kwargs):
# Permite realizar una solicitud HTTP personalizada especificando el método.
response_custom = requests.request("GET", url)
print("\nRespuesta de una solicitud personalizada:")
print(response_custom.json())

# 12. requests.get(url, params=params):
# Envía parámetros en la URL con una solicitud GET.
params = {"userId": 1}
response_params = requests.get(
    "https://jsonplaceholder.typicode.com/posts", params=params)
print("\nRespuesta GET con parámetros:")
print(response_params.json())

# 13. requests.get(url, timeout=segundos):
# Especifica un tiempo de espera para la solicitud.
try:
    response_timeout = requests.get(url, timeout=5)
    print("\nRespuesta GET con tiempo de espera:")
    print(response_timeout.status_code)
except requests.exceptions.Timeout:
    print("\nError: La solicitud excedió el tiempo de espera")

# 14. Manejo de errores con requests.exceptions.RequestException:
# Captura errores generales en solicitudes HTTP.
try:
    response_error = requests.get("https://invalid.url")
except requests.exceptions.RequestException as e:
    print("\nError en la solicitud:", e)
