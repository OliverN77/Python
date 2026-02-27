# 12. Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.

from colorama import init, Fore, Back, Style

def a12():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Comisión escalonada - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        ventas_mensuales = int(input("Ingrese el valor de ventas mensuales: $"))

        if ventas_mensuales > 1000000:
            comision = ventas_mensuales * 0.10
            total = comision * ventas_mensuales
            print(f"La comision total es de ${total}")
        elif ventas_mensuales < 1000000:
            comision = ventas_mensuales * 0.5
            total = comision * ventas_mensuales
            print(f"La comision total es de ${total}")
        else:
            print("Error al interpretar la informacion")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el valor de ventas mensuales.")
if __name__ == "__main__":
    a12()