#Ejercicio 1.5 – Convertidor de unidades con menú: Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.

print("Seleccione una opción:")
print("1. Convertir Celius a Fahrenheit")
print("2. Convertir Kilometros a Millas")
print("3. Convertir Kilogramos a Libras")

op = input("Ingrese el numero de alguna de las opciones: ")
if op == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = float(celsius * 1.8) + 32
    print(f"{celsius} °C son {fahrenheit} °F")
elif op == "2":
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    millas = kilometros * 0.62137
    print(f"{kilometros} km son {millas} millas.")
elif op == "3":
    kilogramos = float(input("Ingrese el peso en kilogramos: "))
    libras = kilogramos * 2.20462
    print(f"{kilogramos} kg son {libras} libras")
else:
    print("Opción no válida. Por favor, seleccione una opcion del 1 a 3.")