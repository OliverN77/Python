# 20. Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.

from colorama import init, Fore, Back, Style

def a20():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Cálculo de intereses simples - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        capital = float(input("Ingrese el capital: "))
        tasa_interes = float(input("Ingrese la tasa de interes: "))
        tiempo_meses = float(input("Ingrese el tiempo en meses: "))

        tasa_interes = tasa_interes / 100

        interes = capital * tasa_interes * tiempo_meses
        total_pagar = capital + interes
        print(f"El interes total generado es: ${total_pagar}")
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
if __name__ == "__main__":
    a20()