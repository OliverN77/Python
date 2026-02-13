# 15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

from colorama import init, Fore, Back, Style

def a15():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Mayor de dos números - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))

        if num1 > num2:
            print(f"El primer numero ({num1}) es mayor que el segundo numero ({num2})")
        elif num2 > num1:
            print(f"El segundo numero ({num2}) es mayor que el primer numero ({num1})")
        else:
            print(f"Los numeros {num1} y {num2} son iguales")
    except ValueError:
        print("Por favor, ingrese solo numeros enteros.")
if __name__ == "__main__":
    a15()