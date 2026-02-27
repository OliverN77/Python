# Tomar el menú de calculadora desarrollado en ejercicios anteriores y refactorizarlo, convirtiendo cada operación matemática en una función separada. El menú principal debe llamar a estas funciones según la opción seleccionada.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    return a / b

print("Calculadora Matemática")
while True:
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "5":
        print("Saliendo ...")
        break

    if opcion in ("1", "2", "3", "4"):
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            continue

        if opcion == "1":
            resultado = sumar(a, b)
            print(f"Resultado: {a} + {b} = {resultado}")
        elif opcion == "2":
            resultado = restar(a, b)
            print(f"Resultado: {a} - {b} = {resultado}")
        elif opcion == "3":
            resultado = multiplicar(a, b)
            print(f"Resultado: {a} * {b} = {resultado}")
        elif opcion == "4":
            resultado = dividir(a, b)
            if resultado is not None:
                print(f"Resultado: {a} / {b} = {resultado}")
    else:
        print("Opción no válida. Intente de nuevo.")
