# 3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.

from colorama import init, Fore, Back, Style

def a3():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Conversión de temperatura - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

        conversion_fahrenheit = float(grados_celsius * 1.8) + 32

        print(f"La temperatura en grados Celsius es: {grados_celsius} °C")
        print(f"La temperatura en grados Fahrenheit es: {conversion_fahrenheit} °F")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la temperatura.")
if __name__ == "__main__":
    a3()