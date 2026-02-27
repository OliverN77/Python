# 23. Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.

from colorama import init, Fore, Back, Style

def a23():
    
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Costo de envío - Algoritmos Python")
    print("By Oliver Nieto")
    print("==" * 20)
    
    try:
        peso_paquete = int(input("Ingrese el peso del paquete: "))

        if peso_paquete <= 5:
            print("El envio cuesta $10.000")
        elif peso_paquete > 5:
            print("El valor del envio es $20.000")
        else:
            print("Información invlaida")
    except ValueError:
        print("Por favor ingrese un valor numérico válido para el peso.")
if __name__ == "__main__":
    a23()