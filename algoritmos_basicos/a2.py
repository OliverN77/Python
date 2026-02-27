# 2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.

from colorama import init, Fore, Back, Style

def a2():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Área de un rectángulo - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))

        area_rectangulo = base * altura
        print(f"El area del triangulo es: {area_rectangulo}")
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
if __name__ == "__main__":
    a2()