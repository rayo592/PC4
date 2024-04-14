import requests
import sqlite3
from datetime import date

def getprice():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  

        data = response.json()  
        precios = {
            'USD': data['bpi']['USD']['rate_float'],  
            'GBP': data['bpi']['GBP']['rate_float'],  
            'EUR': data['bpi']['EUR']['rate_float']  
        }
        return precios
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def creotabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_usd FLOAT,
                        precio_gbp FLOAT,
                        precio_eur FLOAT,
                        precio_pen FLOAT
                    )''')
    conexion.commit()

def insertar_datos_bitcoin(conexion, precios):
    cursor = conexion.cursor()
    fecha_actual = date.today().strftime("%Y-%m-%d")
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                      VALUES (?, ?, ?, ?, ?)''', (fecha_actual, precios['USD'], precios['GBP'], precios['EUR'], 0))  # 0 para precio en PEN
    conexion.commit()

def consultar_precio_compra_bitcoins(conexion, moneda):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT precio_{moneda.lower()} FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    precio_bitcoin = cursor.fetchone()[0]
    return 10 * precio_bitcoin

def main():
    # Se consigue el precio vigente en varias monedas
    precios_bitcoin = getprice()
    if precios_bitcoin is not None:
        # A base de datos SQLite
        conexion = sqlite3.connect('base.db')

        # Creo la tabla 'bitcoin' por si no existe
        creotabla(conexion)
        insertar_datos_bitcoin(conexion, precios_bitcoin)

        precio_compra_pen = consultar_precio_compra_bitcoins(conexion, 'PEN')
        precio_compra_eur = consultar_precio_compra_bitcoins(conexion, 'EUR')

        print(f"Precio de compra de 10 bitcoins en PEN: {precio_compra_pen:.2f} PEN")
        print(f"Precio de compra de 10 bitcoins en EUR: {precio_compra_eur:.2f} EUR")

        conexion.close()

if __name__ == "__main__":
    main()
