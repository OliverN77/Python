# 8. Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.

from colorama import init, Fore, Back, Style

def a8():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Venta con descuento por porcentaje - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:

        precio_producto = int(input("Ingrese el precio del producto: $"))
        porcentaje = int(input("Ingrese el porcentaje de descuento: "))

        descuento = porcentaje / 100
        descuento_aplicado = precio_producto * descuento
        precio_final = precio_producto - descuento_aplicado

        print(f"El descuento del producto es de: {int(descuento * 100)}%")
        print(f"El precio final es: ${int(precio_final)}")
        
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el precio del producto y el porcentaje de descuento.")
if __name__ == "__main__":
    a8()