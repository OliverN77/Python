# Desarrollar un sistema que convierta una calificación numérica (0-100) a su equivalente en letras según la siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Validar que la nota ingresada esté dentro del rango permitido.

calificacion = int(input("Ingrese la calificación numérica (0-100): "))
if 90 <= calificacion <= 100:
    print("La calificación en letras es: A")
elif 80 <= calificacion < 90:
    print("La calificación en letras es: B")
elif 70 <= calificacion < 80:
    print("La calificación en letras es: C")
elif 60 <= calificacion < 70:
    print("La calificación en letras es: D")
elif 0 <= calificacion < 60:
    print("La calificación en letras es: F")
else:
    print("Calificación inválida. Por favor, ingrese un número entre 0 y 100.")