# 22. Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.

from colorama import init, Fore, Back, Style

def a22():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Control de inventario - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        cantidad_inicial = int(input("Ingrese la cantidad inicial de un producto en inventario: "))
        cantidad_vendida = int(input("Ingrese la cantidad vendida de ese producto: "))
        cantidad_recibida = int(input("Ingrese la cantidad recibida de ese producto: "))

        inventario_final = cantidad_inicial + cantidad_recibida - cantidad_vendida
        print(f"El inventario final es: {inventario_final}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
if __name__ == "__main__":
    a22()