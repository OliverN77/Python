# Script para ejecutar todos los ejercicios en secuencia.
# Cada ejercicio se lanza de forma independiente con subprocess para aislar
# el estado y respetar correctamente los bucles interactivos de cada uno.

import subprocess
import sys
import os

EJERCICIOS = [
    ("Sección 1 – Condicionales", [
        ("1.1", "seccion_1/a_1.1.py"),
        ("1.2", "seccion_1/a_1.2.py"),
        ("1.3", "seccion_1/a_1.3.py"),
        ("1.4", "seccion_1/a_1.4.py"),
        ("1.5", "seccion_1/a_1.5.py"),
    ]),
    ("Sección 2 – Condicionales avanzados y menús", [
        ("2.1", "seccion_2/a_2.1.py"),
        ("2.2", "seccion_2/a_2.2.py"),
        ("2.3", "seccion_2/a_2.3.py"),
        ("2.4", "seccion_2/a_2.4.py"),
        ("2.5", "seccion_2/a_2.5.py"),
    ]),
    ("Sección 3 – Bucles", [
        ("3.1", "seccion_3/a_3.1.py"),
        ("3.2", "seccion_3/a_3.2.py"),
        ("3.3", "seccion_3/a_3.3.py"),
        ("3.4", "seccion_3/a_3.4.py"),
        ("3.5", "seccion_3/a_3.5.py"),
    ]),
    ("Sección 4 – Listas y diccionarios", [
        ("4.1", "seccion_4/a_4.1.py"),
        ("4.2", "seccion_4/a_4.2.py"),
        ("4.3", "seccion_4/a_4.3.py"),
        ("4.4", "seccion_4/a_4.4.py"),
        ("4.5", "seccion_4/a_4.5.py"),
    ]),
    ("Sección 5 – Funciones", [
        ("5.1", "seccion_5/a_5.1.py"),
        ("5.2", "seccion_5/a_5.2.py"),
        ("5.3", "seccion_5/a_5.3.py"),
        ("5.4", "seccion_5/a_5.4.py"),
        ("5.5", "seccion_5/a_5.5.py"),
    ]),
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def ejecutar_ejercicio(numero, ruta_relativa):
    ruta = os.path.join(BASE_DIR, ruta_relativa)
    print(f"\n{'=' * 55}")
    print(f"  Ejercicio {numero}  →  {ruta_relativa}")
    print(f"{'=' * 55}\n")
    subprocess.run([sys.executable, ruta], check=False)


def mostrar_menu():
    print("\n╔══════════════════════════════════════════╗")
    print("║   TALLER – Estructuras de Control y      ║")
    print("║             Funciones en Python          ║")
    print("╚══════════════════════════════════════════╝")

    opciones = []
    indice = 1

    for seccion, ejercicios in EJERCICIOS:
        print(f"\n  {seccion}")
        for numero, ruta in ejercicios:
            print(f"    [{indice:2d}] Ejercicio {numero}")
            opciones.append((numero, ruta))
            indice += 1

    print(f"\n    [ 0] Ejecutar todos en secuencia")
    print(f"    [ q] Salir\n")
    return opciones


def main():
    opciones = mostrar_menu()

    while True:
        eleccion = input("Seleccione un ejercicio: ").strip().lower()

        if eleccion == "q":
            print("¡Hasta luego!")
            break
        elif eleccion == "0":
            for numero, ruta in opciones:
                ejecutar_ejercicio(numero, ruta)
            opciones = mostrar_menu()
        else:
            try:
                idx = int(eleccion) - 1
                if 0 <= idx < len(opciones):
                    numero, ruta = opciones[idx]
                    ejecutar_ejercicio(numero, ruta)
                    opciones = mostrar_menu()
                else:
                    print("Número fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingrese un número o 'q'.")


if __name__ == "__main__":
    main()
