import os
import sys
import subprocess
from colorama import init, Fore, Back, Style

while True:
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT)
    print("==" * 20)
    print("Taller 1 - Algoritmos Python")
    print("By Oliver Nieto")
    print("Menú principal")
    print("==" * 20)

    for i in range(1, 26):
        print(f"Ejecutar algoritmo {i}")
    print("0. Salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Saliendo del programa...")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"a{opcion}.py"

        if os.path.exists(archivo):
                subprocess.run([sys.executable, archivo])
        else:
            print(f"No existe {archivo}")
    else:
        print("Opción no válida")
    
    input("\n Presiona ENTER para continuar ...")