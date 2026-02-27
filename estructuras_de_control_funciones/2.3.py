# Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "=" * 50)
print(Fore.CYAN + Style.BRIGHT + "         CALCULADORA MATEMATICA")
print(Fore.CYAN + Style.BRIGHT + "=" * 50)

while True:
    print(Fore.YELLOW + "\n--- Nueva Operación ---")
    num1 = int(input(Fore.GREEN + "Ingrese el primer número: "))
    num2 = int(input(Fore.GREEN + "Ingrese el segundo número: "))
    op = str(input(Fore.MAGENTA + "Ingrese el tipo de operación matemática (suma/resta/multiplicacion/division) o escriba \"salir\": "))

    if op.lower() == "salir":
        print(Fore.RED + Style.BRIGHT + "Saliendo del programa...")
        break

    op = op.lower()

    match op:
        case "suma":
            print(Fore.CYAN + f"✓ La suma es: " + Fore.WHITE + Style.BRIGHT + f"{num1 + num2}")
        case "resta":
            print(Fore.CYAN + f"✓ La resta es: " + Fore.WHITE + Style.BRIGHT + f"{num1 - num2}")
        case "multiplicacion":
            print(Fore.CYAN + f"✓ La multiplicación es: " + Fore.WHITE + Style.BRIGHT + f"{num1 * num2}")
        case "division":
            if num1 == 0 or num2 == 0:
                print(Fore.RED + Style.BRIGHT + f"✗ Error al dividir: No se puede dividir por cero") 
            else:
                print(Fore.CYAN + f"✓ La division es: " + Fore.WHITE + Style.BRIGHT + f"{num1 / num2}")
        case "salir":
            print(Fore.RED + Style.BRIGHT + "Saliendo del programa...")
            break
        case _:
            print(Fore.RED + "✗ Opción no válida. Por favor, intente de nuevo.")

print(Fore.CYAN + Style.BRIGHT + "\n¡Gracias por usar la calculadora!")