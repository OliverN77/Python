# 11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.

from colorama import init, Fore, Back, Style

def a11():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Comisión por ventas - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        ventas_realizadas = int(input("Ingrese el valor de las ventas realizadas: $"))
        comision = ventas_realizadas * 0.05

        total_a_recibir = ventas_realizadas + comision

        print(f"El vendedor recibe un total de ${total_a_recibir}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el valor de las ventas realizadas.")
if __name__ == "__main__":
    a11()