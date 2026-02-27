# 9. Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.

from colorama import init, Fore, Back, Style

def a9():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Venta con IVA - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:

        valor_venta = int(input("Ingrese el valor de la venta: $"))
        iva = valor_venta * 0.19

        total = valor_venta - iva

        print(f"El valor del IVA es: ${iva}, y el total con impuestos es: {total}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el valor de la venta.")
if __name__ == "__main__":
    a9()