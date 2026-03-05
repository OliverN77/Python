# 19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.

from colorama import init, Fore, Back, Style

def a19():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Conversión de moneda - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        valor_cop = int(input("Ingrese un valor en pesos colombianos: "))

        valor_en_usd = valor_cop / 3677

        print(f"{valor_cop} COP en dolares es: {round(valor_en_usd, 2)} USD")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
if __name__ == "__main__":
    a19()