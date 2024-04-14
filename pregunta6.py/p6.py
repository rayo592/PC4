def cuentalineas(archivo):
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            lineas_codigo = 0
            for linea in lineas:
                if linea.strip() != '' and not linea.strip().startswith('#'):
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if ruta_archivo.endswith(".py"):
        lineas_codigo = cuentalineas(ruta_archivo)
        if lineas_codigo is not None:
            print(f"Número de líneas de código en el archivo {ruta_archivo}: {lineas_codigo}")
    else:
        print("El nombre del archivo no termina en .py. Por favor, ingrese un archivo válido.")

if __name__ == "__main__":
    main()
