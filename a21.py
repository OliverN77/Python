# 21. Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.

from colorama import init, Fore, Back, Style

def a21():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Cálculo de intereses compuestos - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        capital = float(input("Ingrese el capital: "))
        tasa_interes = float(input("Ingrese la tasa de interes %: "))
        numero_periodos_tiempo = float(input("Ingrese el numero de periodos (años): "))

        tasa_interes = tasa_interes / 100
        division = tasa_interes / numero_periodos_tiempo
        capital_final = capital * (1 + division) * numero_periodos_tiempo

        print(f"El capital final es de: {capital_final + capital}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
if __name__ == "__main__":
    a21()