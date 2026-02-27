# Crear un algoritmo que solicite la edad de una persona y la clasifique en una de las siguientes categorías: niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto mayor (65 años o más). Mostrar la categoría correspondiente.

edad = int(input("Ingrese su edad: "))

match edad:
    case edad if edad < 0:
        print("La edad no puede ser un número negativo.")
    case edad if edad <= 12:
        print("Eres un niño.")
    case edad if edad <= 17:
        print("Eres un adolescente.")
    case edad if edad <= 64:
        print("Eres un adulto.")
    case edad if edad >= 65:
        print("Eres un adulto mayor.")