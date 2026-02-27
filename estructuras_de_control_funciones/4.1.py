# Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

lista_compras = []
while True:
    print("\nLista de Compras:")
    for i, producto in enumerate(lista_compras, start=1):
        print(f"{i}. {producto}")
    
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1/2/3): ")
    
    if opcion == '1':
        nuevo_producto = input("Ingrese el nombre del producto a agregar: ")
        lista_compras.append(nuevo_producto)
        print(f"{nuevo_producto} ha sido agregado a la lista.")
    
    elif opcion == '2':
        producto_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        if producto_eliminar in lista_compras:
            lista_compras.remove(producto_eliminar)
            print(f"{producto_eliminar} ha sido eliminado de la lista.")
        else:
            print(f"{producto_eliminar} no se encuentra en la lista.")
    
    elif opcion == '3':
        print("¡Gracias por usar el sistema de lista de compras!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")