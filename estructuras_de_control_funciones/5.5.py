# Implementar una función llamada factorial que calcule el factorial de un número usando recursión. La función debe recibir un número entero positivo y retornar su factorial. Incluir validación para números negativos.

def factorial(n):
    if n < 0:
        print("Error: El número debe ser un entero positivo.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = factorial(n - 1)
        return n * result
    
numero = int(input("Ingrese un número entero positivo para calcular su factorial: "))
if numero >= 0:
    print(f"El factorial de {numero} es: {factorial(numero)}")
elif numero == 0:
    print(f"El factorial de {numero} es: {factorial(numero)}")
else:
    print("Error: El número debe ser un entero positivo.")