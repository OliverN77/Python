# 17. Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.

from colorama import init, Fore, Back, Style

def a17():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Edad de una persona - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:

        año_nacimiento = int(input("Ingrese el año de su fecha de nacimiento: "))
        año_actual = int(input("Ingrese el año actual: "))

        edad = año_actual - año_nacimiento

        print(f"Tu edad es de: {edad}")
    except ValueError:
        print("Por favor, ingrese un número válido para el año.")
if __name__ == "__main__":
    a17()