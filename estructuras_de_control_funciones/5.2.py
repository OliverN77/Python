# Implementar una función llamada calcular_promedio que reciba una lista de números como parámetro y retorne el promedio de esos números. Incluir validación para listas vacías.

def calcular_promedio(numeros):
    if len(numeros) == 0:
        print("La lista está vacía. No se puede calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de la lista es: {promedio}")
    
    

numeros = int(input("Ingrese la cantidad de números que desea promediar: "))
lista_numeros = []

for i in range(numeros):
    numero = float(input(f"Ingrese el número {i+1}: "))
    lista_numeros.append(numero)

calcular_promedio(lista_numeros)