# Implementar un menú interactivo con tres opciones: 1. Saludar, 2. Despedirse, 3. Salir. El programa debe mostrar el menú, leer la opción seleccionada y ejecutar la acción correspondiente utilizando estructuras condicionales if-elif-else.

print("Seleccione una opción:")
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

op = input("Ingrese el numero de alguna de las opciones: ")
if op == "1":
    print("¡Hola! ¿Cómo estás?")
elif op == "2":
    print("¡Adiós! Que tengas un buen día.")
elif op == "3":
    print("Saliendo del programa. ¡Hasta luego!")
else:
    print("Opción no válida. Por favor, seleccione una opcion del 1 a 3.")