# Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.

lista1 = []
lista2 = []

while True:
    numero_lista = str(input("Ingrese el numero de la lista a la que desea agregar un elemento (1 o 2) o 3 para salir: "))
    
    if numero_lista == '1':
        elemento = input("Ingrese el elemento a agregar a la lista 1: ")
        lista1.append(elemento)
    elif numero_lista == '2':
        elemento = input("Ingrese el elemento a agregar a la lista 2: ")
        lista2.append(elemento)
    elif numero_lista == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Número de lista inválido. Por favor, ingrese 1 o 2.")
        continue
    continuar = input("¿Desea agregar otro elemento? (s/n): ")
    if continuar.lower() != 's':
        print("Elementos únicos de la lista 1:")
        for elemento in lista1:
            if elemento not in lista2:
                print(f"Elemento único de la lista 1: {elemento}")
        for elemento in lista2:
            if elemento not in lista1:
                print(f"Elemento único de la lista 2: {elemento}")
        print("Elementos comunes a ambas listas:")
        for elemento in lista1:
            if elemento in lista2:
                print(f"Elemento común: {elemento}")
    else:
        continue