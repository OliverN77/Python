# Crear un algoritmo que permita al usuario ingresar 10 números (que pueden repetirse) y luego muestre una lista sin elementos duplicados. Implementar la lógica de eliminación de duplicados usando ciclos y una lista auxiliar, sin utilizar funciones de conjuntos.

numeros = []
for i in range(10):
    n = int(input("Ingrese un número: "))
    numeros.append(n)
    
numeros_sin_duplicados = []
for n in numeros:
    if n not in numeros_sin_duplicados:
        numeros_sin_duplicados.append(n)

print("Lista sin duplicados:", numeros_sin_duplicados)