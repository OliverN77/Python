# 6. Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.

from colorama import init, Fore, Back, Style

def a6():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Total de una venta - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        producto = str(input("Ingrese el nombre del producto: "))
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        total = precio_unitario * cantidad

        print(f"El nombre del producto es: {producto}, cantidad {cantidad} y el valor total a pagar es: {total}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el precio unitario y la cantidad.")
if __name__ == "__main__":
    a6()