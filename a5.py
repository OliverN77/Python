# 5. Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.

from colorama import init, Fore, Back, Style

def a5():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Salario con horas extra - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
        valor_por_hora = int(input("Ingrese el valor por hora: "))
        salario_total = horas_trabajadas * valor_por_hora

        if horas_trabajadas > 40:
            horas_extras = salario_total * 1.5
            total_con_extras = horas_extras + salario_total
            print(f"El valor total de las horas extras es: ${total_con_extras}")
        else :
            print(f"El valor total de las horas extras es: ${salario_total}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para las horas trabajadas y el valor por hora.")
if __name__ == "__main__":
    a5()