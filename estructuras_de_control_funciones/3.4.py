# Desarrollar un programa que solicite al usuario un número y genere su tabla de multiplicar del 1 al 10. Luego, debe preguntar si desea generar otra tabla, continuando este proceso hasta que el usuario decida salir.

n = int(input("Ingrese un número para generar su tabla de multiplicar: "))
print("Para salir del programa, ingrese 'n")

while True:
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
    
    respuesta = input("¿Desea generar otra tabla? (s/n): ")
    if respuesta.lower() != 's':
        print("¡Gracias por usar el programa!")
        break
    
    n = int(input("Ingrese otro número para generar su tabla de multiplicar: "))