# Estructuras de Control y Funciones en Python

Colección de 25 ejercicios prácticos de Python organizados en 5 secciones temáticas. Cubre condicionales, bucles, listas, diccionarios y funciones. Las variables y funciones siguen la convención **snake_case**.

## Estructura del proyecto

```
📁 taller/
├── seccion_1/          → Condicionales (if / elif / else, match/case)
│   ├── a_1.1.py
│   ├── a_1.2.py
│   ├── a_1.3.py
│   ├── a_1.4.py
│   └── a_1.5.py
├── seccion_2/          → Condicionales avanzados y menús interactivos
│   ├── a_2.1.py
│   ├── a_2.2.py
│   ├── a_2.3.py
│   ├── a_2.4.py
│   └── a_2.5.py
├── seccion_3/          → Bucles (for / while)
│   ├── a_3.1.py
│   ├── a_3.2.py
│   ├── a_3.3.py
│   ├── a_3.4.py
│   └── a_3.5.py
├── seccion_4/          → Listas y diccionarios
│   ├── a_4.1.py
│   ├── a_4.2.py
│   ├── a_4.3.py
│   ├── a_4.4.py
│   └── a_4.5.py
└── seccion_5/          → Funciones
    ├── a_5.1.py
    ├── a_5.2.py
    ├── a_5.3.py
    ├── a_5.4.py
    └── a_5.5.py
```

---

## Sección 1 — Condicionales (`if / elif / else`, `match/case`)

| Archivo | Resumen |
|---------|--------|
| [a_1.1.py](taller/seccion_1/a_1.1.py) | Pide nombre, edad y ciudad. Valida que la edad no sea negativa y muestra un saludo personalizado. |
| [a_1.2.py](taller/seccion_1/a_1.2.py) | Calculadora básica con `match/case`: suma, resta, multiplicación y división con control de división por cero. |
| [a_1.3.py](taller/seccion_1/a_1.3.py) | Validador de correo electrónico: verifica que contenga `@` y `.` en posiciones válidas. |
| [a_1.4.py](taller/seccion_1/a_1.4.py) | Validador de contraseña segura: mínimo 8 caracteres, al menos una mayúscula, un número y un carácter especial (`!@#$%^&*`). |
| [a_1.5.py](taller/seccion_1/a_1.5.py) | Convertidor de unidades con menú: °C → °F, km → millas, kg → libras. Muestra el resultado con dos decimales. |

## Sección 2 — Condicionales avanzados y menús interactivos

| Archivo | Resumen |
|---------|--------|
| [a_2.1.py](taller/seccion_2/a_2.1.py) | Clasifica la edad ingresada en: niño (0–12), adolescente (13–17), adulto (18–64) o adulto mayor (65+) usando `match/case`. |
| [a_2.2.py](taller/seccion_2/a_2.2.py) | Menú simple con tres opciones: Saludar, Despedirse y Salir, implementado con `if/elif/else`. |
| [a_2.3.py](taller/seccion_2/a_2.3.py) | Calculadora con bucle `while`: permite varias operaciones seguidas y usa `colorama` para mostrar resultados con color. |
| [a_2.4.py](taller/seccion_2/a_2.4.py) | Convierte una calificación numérica (0–100) a su letra equivalente: A, B, C, D o F. Valida el rango. |
| [a_2.5.py](taller/seccion_2/a_2.5.py) | Simulador de descuentos por categoría: A = 20 %, B = 15 %, C = 10 %. Muestra el monto final y el ahorro. |

## Sección 3 — Bucles (`for` / `while`)

| Archivo | Resumen |
|---------|--------|
| [a_3.1.py](taller/seccion_3/a_3.1.py) | Imprime todos los números pares de 1 a N usando un bucle `while`. |
| [a_3.2.py](taller/seccion_3/a_3.2.py) | Suma acumulada de números ingresados continuamente; se detiene cuando el usuario ingresa 0. |
| [a_3.3.py](taller/seccion_3/a_3.3.py) | Busca un nombre en una lista predefinida con `for` e indica si fue encontrado y en qué posición. |
| [a_3.4.py](taller/seccion_3/a_3.4.py) | Genera la tabla de multiplicar (1–10) del número ingresado; pregunta si se desea generar otra tabla. |
| [a_3.5.py](taller/seccion_3/a_3.5.py) | Recibe 10 números y elimina los duplicados usando una lista auxiliar y bucles, sin `set()`. |

## Sección 4 — Listas y diccionarios

| Archivo | Resumen |
|---------|--------|
| [a_4.1.py](taller/seccion_4/a_4.1.py) | Sistema de lista de compras: agregar productos, eliminar uno específico y mostrar la lista actual. |
| [a_4.2.py](taller/seccion_4/a_4.2.py) | Directorio de contactos con diccionarios (`nombre → teléfono`): agregar, buscar y eliminar contactos. |
| [a_4.3.py](taller/seccion_4/a_4.3.py) | Actualiza el precio de un producto en una lista de diccionarios buscándolo por nombre. |
| [a_4.4.py](taller/seccion_4/a_4.4.py) | Estadísticas de una lista de números ingresados: valor máximo, mínimo, promedio y suma total. |
| [a_4.5.py](taller/seccion_4/a_4.5.py) | Compara dos listas e imprime los elementos comunes, los únicos de cada una; sin usar `set()`. |

## Sección 5 — Funciones

| Archivo | Resumen |
|---------|--------|
| [a_5.1.py](taller/seccion_5/a_5.1.py) | Función `saludar(nombre, hora)`: devuelve "Buenos días", "Buenas tardes" o "Buenas noches" según la hora. |
| [a_5.2.py](taller/seccion_5/a_5.2.py) | Función `calcular_promedio(numeros)`: retorna el promedio de una lista; valida si la lista está vacía. |
| [a_5.3.py](taller/seccion_5/a_5.3.py) | Calculadora refactorizada: cada operación (`sumar`, `restar`, `multiplicar`, `dividir`) es una función separada. |
| [a_5.4.py](taller/seccion_5/a_5.4.py) | Función `es_palindromo(texto)`: retorna `True`/`False` ignorando espacios, mayúsculas y puntuación. |
| [a_5.5.py](taller/seccion_5/a_5.5.py) | Función `factorial(n)`: calcula el factorial de forma recursiva con validación para números negativos. |

---

## Convenciones de código

- Nombres de variables y funciones en **snake_case** (`lista_compras`, `calcular_promedio`)
- Condicionales con `if / elif / else` y `match/case` (Python 3.10+)
- Bucles `for` y `while` para iteraciones y menús interactivos
- Funciones con parámetros explícitos y validación de entrada
- Cada archivo expone una función **`run()`** como punto de entrada y utiliza el patrón `if __name__ == "__main__": run()` para poder ejecutarse de forma directa o ser importado desde `run_all.py`

## Ejecución

### Ejecutar un ejercicio individual

```bash
python taller/seccion_1/a_1.1.py
```

### Ejecutar todos los ejercicios desde el menú interactivo

```bash
python taller/run_all.py
```

El script `run_all.py` presenta un menú numerado con los 25 ejercicios. Se puede elegir uno en particular o ejecutarlos todos en secuencia (opción `0`).

## Requisitos

- Python **3.10** o superior
- Dependencias externas listadas en `requirements.txt`

```bash
pip install -r requirements.txt
```
