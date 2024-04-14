import requests
import sqlite3

def obtener_datos_tipo_cambio_2023():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    parametros = {"fecha": "2023-01-01", "hasta": "2023-12-31"}
    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()
        datos = response.json()
        return datos
    except requests.RequestException as e:
        print("Error al obtener los datos del tipo de cambio:", e)
        return None

def crear_tabla_sunat_info(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        precio_compra FLOAT,
                        precio_venta FLOAT
                    )''')
    conexion.commit()

def insertar_datos_sunat_info(conexion, datos):
    cursor = conexion.cursor()
    for fecha, valores in datos.items():
        precio_compra = valores.get('precioCompra', 0)
        precio_venta = valores.get('precioVenta', 0)
        cursor.execute('''INSERT INTO sunat_info (fecha, precio_compra, precio_venta)
                          VALUES (?, ?, ?)''', (fecha, precio_compra, precio_venta))
    conexion.commit()

def mostrar_contenido_tabla_sunat_info(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def main():
    # Obtener los datos de tipo de cambio del año 2023
    datos_tipo_cambio = obtener_datos_tipo_cambio_2023()
    if datos_tipo_cambio:
        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('base.db')

        # Crear la tabla 'sunat_info' si no existe
        crear_tabla_sunat_info(conexion)

        # Insertar los datos en la tabla 'sunat_info'
        insertar_datos_sunat_info(conexion, datos_tipo_cambio)

        # Mostrar el contenido de la tabla 'sunat_info'
        mostrar_contenido_tabla_sunat_info(conexion)

        # Cerrar la conexión a la base de datos
        conexion.close()

if __name__ == "__main__":
    main()

