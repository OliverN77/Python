# 25. Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.

from colorama import init, Fore, Back, Style

def a25():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Venta diaria de un almacén - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        numero_ventas = int(input("Ingrese el número de ventas realizadas en el día: "))
        ventas = []

        for i in range(numero_ventas):
            i = i+1
            valor_venta = int(input(f"Ingrese el valor de la venta del producto {i}: $"))
            ventas.append(valor_venta)

        total_vendido = sum(ventas)

        promedio_ventas = total_vendido / numero_ventas
        
        print("-" * 40)
        print(f"El total vendido es de: ${total_vendido}")
        print(f"El promedio de ventas es de: ${promedio_ventas}")
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el número de ventas y el valor de cada venta.")
if __name__ == "__main__":
    a25()