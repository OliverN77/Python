# Descripción del sistema: Desarrollar un programa completo en Python para gestionar los libros de una biblioteca, aplicando todos los conceptos aprendidos en las secciones anteriores. El sistema debe permitir realizar operaciones básicas de mantenimiento de un catálogo bibliográfico.

"""Requisitos funcionales:
- Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener: id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).

- Funciones principales: o agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900. 

o mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]".
o buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales.

o prestar_libro(id): Cambia el estado de disponibilidad a False si el libro existe y está disponible. 
o devolver_libro(id): Cambia el estado de disponibilidad a True. 
o eliminar_libro(id): Elimina un libro solo si no está prestado actualmente. 
o menu_principal(): Implementa un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.
- Funciones adicionales desafiantes: o libros_por_autor(autor): Lista todos los libros de un autor específico. 
o estadisticas(): Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados. 
o exportar_a_txt(): Guarda todos los libros en un archivo de texto llamado "biblioteca.txt"."""

from colorama import init, Fore, Back, Style
init(autoreset=True)

# Colores reutilizables
EXITO   = Fore.GREEN  + Style.BRIGHT
ERROR   = Fore.RED    + Style.BRIGHT
AVISO   = Fore.YELLOW + Style.BRIGHT
INFO    = Fore.CYAN   + Style.BRIGHT
TITULO  = Fore.MAGENTA + Style.BRIGHT
OPCION  = Fore.WHITE  + Style.BRIGHT
PROMPT  = Fore.CYAN
RESET   = Style.RESET_ALL

# Estructura de datos: lista que contiene diccionarios (un diccionario por libro)
biblioteca = []  # Lista vacía - cada elemento será un diccionario representando un libro
contador_id = 0  # Renombrado para no pisarlo con el parámetro 'id' de las funciones

def _formato_libro(libro, indent=""):
    if libro["disponible"]:
        estado_color = Fore.GREEN + Style.BRIGHT + "Disponible" + RESET
    else:
        estado_color = Fore.RED + Style.BRIGHT + "Prestado" + RESET
    id_str    = Fore.YELLOW + Style.BRIGHT + f"ID: {libro['id']}" + RESET
    detalle   = Fore.WHITE  + f" - '{libro['titulo']}' ({libro['autor']}, {libro['año']})" + RESET
    return f"{indent}{id_str}{detalle} [{estado_color}]"

def agregar_libro():
    global biblioteca, contador_id
    print(INFO + "\n── Agregar libro ──")
    titulo = str(input(PROMPT + "Ingrese el título del libro: " + RESET))
    autor  = str(input(PROMPT + "Ingrese el autor del libro: "  + RESET))

    while True:
        año = input(PROMPT + "Ingrese el año de publicación (numérico y mayor a 1900): " + RESET)
        if año.isdigit() and int(año) > 1900:
            año = int(año)
            break
        else:
            print(ERROR + "Año inválido. Por favor, ingrese un año numérico mayor a 1900.")

    contador_id += 1
    # Se crea un diccionario con la información del libro y se agrega a la lista
    libro = {
        "id": contador_id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "disponible": True
    }
    biblioteca.append(libro)  # Se agrega el diccionario a la lista
    print(EXITO + f"✔ Libro '{titulo}' agregado exitosamente con ID {contador_id}.")

def mostrar_libros():
    print(INFO + "\n── Catálogo de libros ──")
    if biblioteca:
        for libro in biblioteca:  # Se recorre cada diccionario de la lista
            print(_formato_libro(libro))
    else:
        print(AVISO + "No hay libros en la biblioteca.")

def buscar_libro():
    busqueda = input(PROMPT + "\nIngrese el título o autor del libro a buscar: " + RESET).lower()
    encontrados = [
        libro for libro in biblioteca  # Filtra la lista buscando coincidencias parciales
        if busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower()
    ]
    if encontrados:
        print(INFO + f"Libros encontrados ({len(encontrados)}):")
        for libro in encontrados:
            print(_formato_libro(libro, indent="  "))
    else:
        print(ERROR + "No se encontraron libros que coincidan con la búsqueda.")

def prestar_libro(id):
    for libro in biblioteca:  # Se busca en la lista el libro con ese id
        if libro["id"] == id:
            if libro["disponible"]:
                libro["disponible"] = False
                print(EXITO + "✔ Libro prestado exitosamente.")
            else:
                print(ERROR + "✘ El libro ya está prestado.")
            return
    print(ERROR + "✘ No se encontró el libro con el ID proporcionado.")

def devolver_libro(id):
    for libro in biblioteca:
        if libro["id"] == id:
            if not libro["disponible"]:
                libro["disponible"] = True
                print(EXITO + "✔ Libro devuelto exitosamente.")
            else:
                print(AVISO + "El libro ya está disponible (aún no se ha prestado).")
            return
    print(ERROR + "✘ No se encontró el libro con el ID proporcionado.")

def eliminar_libro(id):
    for libro in biblioteca:
        if libro["id"] == id:
            if not libro["disponible"]:
                print(ERROR + "✘ No se puede eliminar un libro que está prestado.")
            else:
                biblioteca.remove(libro)  # Se elimina el diccionario de la lista
                print(EXITO + "✔ Libro eliminado exitosamente.")
            return
    print(ERROR + "✘ No se encontró el libro con el ID proporcionado.")

def libros_por_autor(autor):
    encontrados = [libro for libro in biblioteca if autor.lower() in libro["autor"].lower()]
    if encontrados:
        print(INFO + f"\nLibros del autor '{autor}':")
        for libro in encontrados:
            print(_formato_libro(libro, indent="  "))
    else:
        print(ERROR + f"✘ No se encontraron libros del autor '{autor}'.")

def estadisticas():
    total      = len(biblioteca)
    disponibles = sum(1 for libro in biblioteca if libro["disponible"])
    prestados  = total - disponibles
    print(INFO + "\n── Estadísticas de la biblioteca ──")
    print(OPCION + f"  Total de libros:    " + Fore.WHITE  + str(total))
    print(OPCION + f"  Libros disponibles: " + Fore.GREEN  + Style.BRIGHT + str(disponibles))
    print(OPCION + f"  Libros prestados:   " + Fore.RED    + Style.BRIGHT + str(prestados))
    print()

def exportar_a_txt():
    with open("biblioteca.txt", "w", encoding="utf-8") as archivo:
        for libro in biblioteca:  # Se recorre la lista y se escribe cada libro
            estado = "Disponible" if libro["disponible"] else "Prestado"
            archivo.write(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['año']}) [{estado}]\n")
    print(EXITO + "✔ Libros exportados a biblioteca.txt exitosamente.")

def menu_principal():
    while True:
        print(TITULO + "\n" + "=" * 40)
        print(TITULO + "   📚  Sistema de Gestión de Biblioteca")
        print(TITULO + "=" * 40)
        opciones = [
            ("1", "Agregar libro"),
            ("2", "Mostrar libros"),
            ("3", "Buscar libro"),
            ("4", "Prestar libro"),
            ("5", "Devolver libro"),
            ("6", "Eliminar libro"),
            ("7", "Listar libros por autor"),
            ("8", "Estadísticas"),
            ("9", "Exportar a TXT"),
            ("0", "Salir"),
        ]
        for num, desc in opciones:
            color = Fore.RED + Style.BRIGHT if num == "0" else Fore.CYAN
            print(f"  {color}{num}. {Fore.WHITE}{desc}{RESET}")
        print(TITULO + "=" * 40)

        opcion = input(PROMPT + "Seleccione una opción: " + RESET)

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            prestar_libro(int(input(PROMPT + "Ingrese el ID del libro a prestar: "   + RESET)))
        elif opcion == "5":
            devolver_libro(int(input(PROMPT + "Ingrese el ID del libro a devolver: " + RESET)))
        elif opcion == "6":
            eliminar_libro(int(input(PROMPT + "Ingrese el ID del libro a eliminar: " + RESET)))
        elif opcion == "7":
            libros_por_autor(input(PROMPT + "Ingrese el nombre del autor: " + RESET))
        elif opcion == "8":
            estadisticas()
        elif opcion == "9":
            exportar_a_txt()
        elif opcion == "0":
            print(AVISO + "\nSaliendo...")
            break
        else:
            print(ERROR + "✘ Opción no válida. Ingrese un número del 0 al 9.")

        input(Fore.WHITE + Style.DIM + "\nPresiona ENTER para continuar..." + RESET)

if __name__ == "__main__":
    menu_principal()