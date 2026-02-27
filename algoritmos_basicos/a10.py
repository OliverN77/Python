# 10. Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.

from colorama import init, Fore, Back, Style

def a10():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Compra de varios productos - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
        # Almacenar los precios de los productos en una lista
        productos = []

        # Solicitar el precio de cada producto y almacenarlo en la lista
        for i in range(cantidad_productos):
            precio = int(input(f"Ingrese el precio del producto {i+1}: $"))
            productos.append(precio)
            
        # Calcular el total de la compra sumando los precios de los productos
        total_compra = sum(productos)
        print("-" * 40)
        print(f"El total de la compra es: ${total_compra}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la cantidad de productos y el precio de cada uno.")
if __name__ == "__main__":
    a10()