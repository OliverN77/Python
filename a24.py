# 24. Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.

from colorama import init, Fore, Back, Style

def a24():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Factura de servicios públicos - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        consumo_agua = int(input("Ingrese el consumo del agua en metro cúbicos: "))
        valor_por_metro_cubico = int(input("Ingrese el valor por metro cúbico: "))

        calculo = consumo_agua * valor_por_metro_cubico

        print(f"El valor total de la factura es de: ${calculo}")
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el consumo y el valor por metro cúbico.")
if __name__ == "__main__":
    a24()