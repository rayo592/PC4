import requests
import json
from datetime import datetime

def prec_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  #se verifica por si hay errores 

        data = response.json()  #cambiamos de formato a json
        priceusd = data['bpi']['USD']['rate']  #precio de Bitcoin en USD
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actual

        return priceusd, timestamp
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None, None

def guardar_datos_en_archivo(precio, timestamp):
    try:
        with open("bitcoin_prices.txt", "a") as file:
            file.write(f"Fecha y hora: {timestamp}, Precio de Bitcoin (USD): {precio}\n")
        print("Datos guardados correctamente en bitcoin_prices.txt")
    except Exception as e:
        print("Error al guardar los datos en el archivo:", e)

def main():
    precio, timestamp = prec_bitcoin()

    # Guardo los datos en archivo texto
    if precio is not None and timestamp is not None:
        guardar_datos_en_archivo(precio, timestamp)

if __name__ == "__main__":
    main()
