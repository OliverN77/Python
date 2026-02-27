# Crear un directorio de contactos utilizando diccionarios, donde cada contacto tenga un nombre (clave) y un número telefónico (valor). El sistema debe permitir agregar nuevos contactos, buscar contactos por nombre y eliminar contactos existentes.

contactos = {}

while True:
    print("\nDirectorio de Contactos:")
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")
    
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion == '1':
        nombre_nuevo = input("Ingrese el nombre del nuevo contacto: ")
        telefono_nuevo = input("Ingrese el número telefónico del nuevo contacto: ")
        contactos[nombre_nuevo] = telefono_nuevo
        print(f"{nombre_nuevo} ha sido agregado al directorio.")
    
    elif opcion == '2':
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        if nombre_buscar in contactos:
            print(f"{nombre_buscar}: {contactos[nombre_buscar]}")
        else:
            print(f"{nombre_buscar} no se encuentra en el directorio.")
    
    elif opcion == '3':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre_eliminar in contactos:
            del contactos[nombre_eliminar]
            print(f"{nombre_eliminar} ha sido eliminado del directorio.")
        else:
            print(f"{nombre_eliminar} no se encuentra en el directorio.")
    
    elif opcion == '4':
        print("¡Gracias por usar el directorio de contactos!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")