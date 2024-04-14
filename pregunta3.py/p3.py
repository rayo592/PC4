import requests
import zipfile
from io import BytesIO
import os

# URL de la imagen
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen desde la URL
response = requests.get(url)
image_data = response.content

# Guardar la imagen en un archivo
with open("imagen.jpg", "wb") as file:
    file.write(image_data)

# Crear un archivo ZIP y agregar la imagen
with zipfile.ZipFile("imagenes.zip", "w") as zip_file:
    zip_file.write("imagen.jpg")

# Descomprimir el archivo ZIP
with zipfile.ZipFile("imagenes.zip", "r") as zip_ref:
    zip_ref.extractall("imagenes_descomprimidas")

# Eliminar la imagen original y el archivo ZIP
os.remove("imagen.jpg")
os.remove("imagenes.zip")

print("Proceso completado. La imagen se ha descargado, almacenado como archivo ZIP y luego descomprimido.")
 
