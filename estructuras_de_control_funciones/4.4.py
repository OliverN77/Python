# Desarrollar un programa que solicite al usuario ingresar una lista de números separados por comas. El algoritmo debe calcular y mostrar: el valor máximo, el valor mínimo, el promedio y la suma total de todos los números.

numeros = []

while True:
    agregar_numero = float(input("Ingrese un número para agregarlo a la lista: "))
    numeros.append(agregar_numero)
    respuesta = input("¿Desea agregar otro número? (s/n): ")
    if respuesta.lower() == 's':
        continue
    else:
        maximo = max(numeros)
        minimo = min(numeros)
        promedio = sum(numeros) / len(numeros)
        suma_total = sum(numeros)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
        print(f"El promedio es: {promedio}")
        print(f"La suma total es: {suma_total}")
        break