# Dada una lista de diccionarios donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock", crear un programa que permita actualizar el precio de un producto específico buscándolo por su nombre.

productos = {
    "nombre": "Arroz",
    "precio": 100,
    "stock": 50
}

while True:
    print("\nProducto actual:")
    for clave, valor in productos.items():
        print(f"{clave}: {valor}")
        
    print("1. Actualizar Nombre")
    print("2. Actualizar precio")
    print("3. Actualizar stock")
    print("4. Salir")
        
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        productos["nombre"] = nuevo_nombre
        print(f"El nombre del producto ha sido actualizado a '{productos['nombre']}'.")
    elif opcion == '2':
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        productos["precio"] = nuevo_precio
        print(f"El precio del producto '{productos['nombre']}' ha sido actualizado a {nuevo_precio}.")
    elif opcion == '3':
        nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
        productos["stock"] = nuevo_stock
        print(f"El stock del producto '{productos['nombre']}' ha sido actualizado a {nuevo_stock}.")
    elif opcion == '4':
        print("Saliendo ...")
        break