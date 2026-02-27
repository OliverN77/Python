# 14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.

from colorama import init, Fore, Back, Style

def a14():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Nota final ponderada - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        talleres = float(input("Ingrese la nota de los talleres: "))
        examen_parcial = float(input("Ingrese la nota del examen parcial: "))
        examen_final = float(input("Ingrese la nota del examen final: "))

        nota_final = (talleres * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)
        print(f"La nota final es: {nota_final}")
    except ValueError:
        print("Por favor, ingrese un número válido para las notas.")
if __name__ == "__main__":
    a14()