# 18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.

from colorama import init, Fore, Back, Style

def a18():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Clasificación por edad - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:

        edad = int(input("Ingrese su edad: "))

        if edad < 18:
            print(f"Tu edad ({edad}), es igual a la de un menor de edad")
        elif edad >= 18 and edad < 60:
            print(f"Tu edad ({edad}), es igual a la de un adulto")
        elif edad >= 60:
            print(f"Tu edad ({edad}), es igual a la de un adulto mayor")
        else:
            print(f"{edad}, es invalido")
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")
a18()