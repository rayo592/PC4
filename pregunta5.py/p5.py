def guardotabmu(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{numero} x {i} = {numero * i}\n")
        print(f"La tabla de multiplicar del número {numero} ha sido guardada en tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def showtabmult(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            print(f"Tabla de multiplicar del número {numero}:")
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def showlinemult(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if len(lineas) >= linea:
                print(f"Línea {linea} de la tabla de multiplicar del número {numero}: {lineas[linea - 1]}")
            else:
                print(f"La tabla de multiplicar del número {numero} no tiene {linea} líneas.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            guardotabmu(numero)
        elif opcion == '2':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            showtabmult(numero)
        elif opcion == '3':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            showlinemult(numero, linea)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()

