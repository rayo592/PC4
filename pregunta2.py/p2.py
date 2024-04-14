from pyfiglet import Figlet
import random

def foint():
    figlet = Figlet()
    fuentes = figlet.getFonts()

    fuente = input("Ingrese el nombre de una fuente (o presione Enter para seleccionar aleatoriamente): ")
    if not fuente:
        fuente = random.choice(fuentes)

    return fuente

def main():
    fuente = foint()

    texto = input("Ingrese el texto a imprimir: ")

    figlet = Figlet()
    figlet.setFont(font=fuente)

    # Imprimo texto con la fuente
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()

