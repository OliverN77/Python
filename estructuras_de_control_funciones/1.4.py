# Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

password = str(input("Ingrese su contraseña: "))
special_charts = "!@#$%^&*"

is_opper = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special_charts = any(char in special_charts for char in password)

if len(password) < 8:
    print("La contraseña debe tener por lo menos 8 caracteres.")
elif is_opper == False:
    print("La contraseña debe tener por lo menos una letra mayúscula.")
elif has_number == False:
    print("La contraseña debe tener por lo menos un número.")
elif has_special_charts == False:
    print("La contraseña debe tener por lo menos un carácter especial.")
else:
    print("La contraseña está correcta.")
