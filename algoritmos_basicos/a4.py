# 4. Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.

from colorama import init, Fore, Back, Style

def a4():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Salario semanal - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        horas_trabajo = float(input("Ingrese la cantidad de horas trabajadas en la semana: "))
        valor_por_hora = float(input("Ingrese el valor por hora: "))

        salario_semanal = horas_trabajo * valor_por_hora
        print(f"El salario semanal es: ${salario_semanal}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para las horas trabajadas y el valor por hora.")
if __name__ == "__main__":
    a4()