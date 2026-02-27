# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

n = int(input("Ingrese un número entero positivo: "))

contador = 0
print(contador)

while contador < n:
    contador = contador + 1
    
    if contador %2 == 0:
        print(contador)