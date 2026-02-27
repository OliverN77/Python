num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
op = str(input("Ingrese el tipo de operación matemática (no el simbolo): "))

op = op.lower()

match op:
    case "suma":
        print(f"La suma es: {num1 + num2}")
    case "resta":
        print(f"La resta es: {num1 - num2}")
    case "multiplicacion":
        print(f"La multiplicación es: {num1 * num2}")
    case "division":
        if num1 == 0 or num2 == 0:
            print(f"Error al dividir: {ZeroDivisionError}") 
        else:
            print(f"La division es: {num1 / num2}")