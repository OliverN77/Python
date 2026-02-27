# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.

nombres = ["Oliver", "Emmanuel", "Kevin", "Juan Manuel"]
input_nombre = str(input("Ingrese el nombre que desea buscar: "))
input_nombre = input_nombre.capitalize()

for nombre in nombres:
    if nombre == input_nombre:
        print("El nombre se encuentra en la lista.")
        print("Posición:", nombres.index(nombre))
        break
    else:
        continue
else:
    print("El nombre no se encuentra en la lista.")