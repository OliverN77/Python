# 7. Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.

from colorama import init, Fore, Back, Style

def a7():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Venta con descuento fijo - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        valor_total = int(input("Ingrese el valor total de la compra: "))

        if valor_total > 200000:
            descuento = valor_total * 0.10
            precio_con_descuento = valor_total - descuento
            print(f"El total con descuento es: {precio_con_descuento}")
        else:
            print(f"El valor total es: {valor_total}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el valor total de la compra.")
if __name__ == "__main__":
    a7()