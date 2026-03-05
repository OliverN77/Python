# 13. Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).

from colorama import init, Fore, Back, Style

def a13():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Promedio de notas - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:

        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 3.0:
            print(f"El estudiante aprueba con un proemdio de: {promedio}")
        elif promedio < 3.0:
            print(f"El estudiante no aprueba tiene un promedio de: {promedio}")
        else:
            print("Error al ingresar notas.")
    except ValueError:
        print("Por favor, ingrese un número válido para las notas.")
if __name__ == "__main__":
    a13()