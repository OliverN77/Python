# 16. Número par o impar: Solicitar un número entero e indicar si es par o impar.

from colorama import init, Fore, Back, Style

def a16():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Número par o impar - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        numero = int(input("Ingrese un numero entero: "))

        if numero %2==0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} es impar (no par)")
    except ValueError:
        print("Error: Por favor ingrese un numero entero valido.")
if __name__ == "__main__":
    a16()