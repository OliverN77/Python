#Ejercicio 1.3 – Validación de correo electrónico: Crear un programa que pida al usuario ingresar un correo electrónico y verifique que contenga los caracteres "@" y "." en posiciones válidas. Mostrar mensajes apropiados indicando si el correo tiene un formato básico correcto o si presenta errores.


correo = str(input("Ingrese el correo electrónico: "))
caracteres = [car for car in correo]

if '@' in correo and '.' in correo:
    pos_arroba = correo.index('@')
    pos_punto = correo.index('.')
    
    if pos_arroba > 0 and pos_punto > pos_arroba + 1 and pos_punto < len(correo) - 1:
        caracter_anterior = correo[pos_arroba - 1]
        print("Correo válido.")
    else:
        print("Formato de correo inválido.")

else:
    print("No hay punto o arroba en el correo.")