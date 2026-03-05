# Solicitar: nombre, edad y ciudad. Mostrar

def run():
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    ciudad_residencia = str(input("Ingrese  la ciudad de residencia: "))

    if edad < 0:
        print("La edad no puede ser un número negativo.")
    else:
        print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad_residencia}.")


if __name__ == "__main__":
    run()