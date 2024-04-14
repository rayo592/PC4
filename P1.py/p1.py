import requests

def price_bit():
    try:
        # Vemos en la API para conseguir el precio actual
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Verificar si hay errores en la solicitud

        data = response.json()  
        precio_en_usd = data['bpi']['USD']['rate_float']  # precio en dolares

        return precio_en_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    try:
        bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
        return

    precio_bitcoin = price_bit()
    if precio_bitcoin is not None:
        # cantidad de bitcoins por precio del bitcoin
        costo_en_usd = bitcoins * precio_bitcoin
        print(f"El costo actual de {bitcoins} bitcoins en USD es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
