# 🐍 Curso Python - Ejercicios y Talleres

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Colorama](https://img.shields.io/badge/Colorama-Latest-green.svg)](https://pypi.org/project/colorama/)
[![License](https://img.shields.io/badge/Licencia-Educativa-orange.svg)](#)

Repositorio de ejercicios y talleres prácticos del curso de Python que cubre desde fundamentos de programación hasta proyectos integradores. Cada sección está diseñada para reforzar conceptos progresivos del lenguaje.

**Desarrollado por:** Oliver Nieto Osorio - 3406211

---

## 📁 Estructura del Repositorio

```
Python/
│
├── taller1_algoritmos_basicos/              # Taller 1 - 25 algoritmos fundamentales
│   ├── index.py                             # Menú principal interactivo
│   ├── a1.py  →  a25.py                     # Algoritmos individuales (1 al 25)
│   └── README.md                            # Documentación detallada del taller
│
└── taller2_Estructuras de control y Funciones/  # Taller 2 - Estructuras de control y funciones
    ├── requirements.txt                         # Dependencias del taller
    ├── README.md                                # Documentación del taller
    ├── taller/                                  # Ejercicios del taller
    │   ├── run_all.py                           # Script para ejecutar todos los ejercicios
    │   ├── seccion_1/                           # Sección 1: Variables y entrada/salida
    │   │   └── a_1.1.py  →  a_1.5.py
    │   ├── seccion_2/                           # Sección 2: Estructuras condicionales
    │   │   └── a_2.1.py  →  a_2.5.py
    │   ├── seccion_3/                           # Sección 3: Ciclos (for / while)
    │   │   └── a_3.1.py  →  a_3.5.py
    │   ├── seccion_4/                           # Sección 4: Listas y estructuras de datos
    │   │   └── a_4.1.py  →  a_4.5.py
    │   └── seccion_5/                           # Sección 5: Funciones y recursión
    │       └── a_5.1.py  →  a_5.5.py
    └── seccion_6_mini_taller/                   # Mini Taller Integrador
        ├── gestion_biblioteca.py                # Sistema de gestión de biblioteca
        └── biblioteca.txt                       # Archivo de datos exportados
```

---

## 📂 Módulos del Proyecto

### 📘 1. Algoritmos Básicos (`taller1_algoritmos_basicos/`)

Colección de **25 algoritmos** que cubren los fundamentos de la programación en Python: operaciones matemáticas, cálculos de salario y comisiones, gestión de ventas, manejo académico y conversiones financieras.

**Características:**
- Menú interactivo principal (`index.py`) para navegar entre todos los algoritmos
- Interfaz colorida en terminal usando `colorama`
- Validación de entradas y manejo de excepciones en cada ejercicio

**Temas cubiertos:**
| Categoría | Algoritmos |
|---|---|
| Operaciones Matemáticas | Suma/promedio, área, conversión de temperatura |
| Salario y Comisiones | Salario semanal, horas extra, comisiones escalonadas |
| Ventas y Descuentos | Descuentos, IVA (19%), múltiples productos |
| Gestión Académica | Promedio de notas, calificación ponderada |
| Comparaciones | Mayor/menor, par/impar, clasificación por edad |
| Finanzas | Conversión de moneda, interés simple e interés compuesto |
| Logística | Control de inventario, costo de envío, factura de servicios |

> Para más detalles, revisar el [README interno](taller1_algoritmos_basicos/README.md).

---

### 📗 2. Estructuras de Control y Funciones (`taller2_Estructuras de control y Funciones/`)

**25 ejercicios** organizados en 5 secciones temáticas para practicar las estructuras fundamentales de Python.

**Sección 1 — Variables y Entrada/Salida (`taller/seccion_1/a_1.x`)**
- Manejo de tipos de datos: `str`, `int`, `float`
- Solicitud y presentación de datos al usuario
- Formateo de salida con f-strings

**Sección 2 — Estructuras Condicionales (`taller/seccion_2/a_2.x`)**
- Uso de `if`, `elif`, `else` y `match`
- Clasificación por rangos (edades, categorías)
- Toma de decisiones con operadores lógicos y de comparación

**Sección 3 — Ciclos (`taller/seccion_3/a_3.x`)**
- Bucles `for` y `while`
- Iteración sobre rangos y secuencias
- Control de flujo con `break` y `continue`

**Sección 4 — Listas y Estructuras de Datos (`taller/seccion_4/a_4.x`)**
- Creación y manipulación de listas
- Operaciones CRUD sobre colecciones
- Uso de `enumerate`, búsqueda y ordenamiento

**Sección 5 — Funciones y Recursión (`taller/seccion_5/a_5.x`)**
- Definición y llamado de funciones
- Parámetros, retorno de valores y scope
- Recursión aplicada (ej: cálculo de factorial)

---

### 📙 3. Mini Taller Integrador (`taller2_Estructuras de control y Funciones/seccion_6_mini_taller/`)

Sistema completo de **gestión de biblioteca** que integra todos los conceptos aprendidos.

**Funcionalidades:**
| Función | Descripción |
|---|---|
| `agregar_libro()` | Registra un nuevo libro con validación de año (> 1900) |
| `mostrar_libros()` | Lista todos los libros con su estado de disponibilidad |
| `buscar_libro()` | Búsqueda parcial por título o autor |
| `prestar_libro(id)` | Cambia el estado a *Prestado* si está disponible |
| `devolver_libro(id)` | Marca el libro como *Disponible* nuevamente |
| `eliminar_libro(id)` | Elimina un libro solo si no está prestado |
| `libros_por_autor(autor)` | Lista todos los libros de un autor específico |
| `estadisticas()` | Muestra totales: libros disponibles y prestados |
| `exportar_a_txt()` | Exporta el catálogo completo a `biblioteca.txt` |

**Estructura de datos utilizada:** Lista de diccionarios con campos `id`, `titulo`, `autor`, `año` y `disponible`.

---

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.14.3 o superior
- `colorama` (requerido solo para `taller1_algoritmos_basicos/`)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/OliverN77/Python.git
cd Python

# Instalar dependencias
pip install colorama
```

### Ejecución

```bash
# Taller 1 - Menú interactivo de algoritmos básicos
cd taller1_algoritmos_basicos
python index.py

# Taller 1 - Ejecutar un algoritmo individual
python a1.py

# Taller 2 - Ejecutar todos los ejercicios
cd "taller2_Estructuras de control y Funciones/taller"
python run_all.py

# Taller 2 - Ejecutar un ejercicio específico
cd "taller2_Estructuras de control y Funciones/taller/seccion_1"
python a_1.1.py

# Mini Taller - Sistema de gestión de biblioteca
cd "taller2_Estructuras de control y Funciones/seccion_6_mini_taller"
python gestion_biblioteca.py
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.14.3** — Lenguaje de programación principal
- **Colorama** — Colorización de texto en terminal
- **f-strings** — Formateo moderno de cadenas
- **Try-Except** — Manejo robusto de excepciones
- **Archivos `.txt`** — Persistencia de datos en el mini taller

---

## 👨‍💻 Autor

**Oliver Nieto Osorio**  
Código estudiantil: 3406211

---

## 📄 Licencia

Este proyecto está disponible con fines educativos y de aprendizaje.
