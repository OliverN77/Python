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
├── algoritmos_basicos/              # Taller 1 - 25 algoritmos fundamentales
│   ├── index.py                     # Menú principal interactivo
│   ├── a1.py  →  a25.py             # Algoritmos individuales (1 al 25)
│   └── README.md                    # Documentación detallada del taller
│
├── estructuras_de_control_funciones/ # Taller 2 - Estructuras de control y funciones
│   ├── 1.1.py  →  1.5.py            # Sección 1: Variables y entrada/salida
│   ├── 2.1.py  →  2.5.py            # Sección 2: Estructuras condicionales
│   ├── 3.1.py  →  3.5.py            # Sección 3: Ciclos (for / while)
│   ├── 4.1.py  →  4.5.py            # Sección 4: Listas y estructuras de datos
│   └── 5.1.py  →  5.5.py            # Sección 5: Funciones y recursión
│
└── mini_taller_integrador/          # Mini Taller Integrador
    ├── gestion_biblioteca.py        # Sistema de gestión de biblioteca
    └── biblioteca.txt               # Archivo de datos exportados
```

---

## 📂 Módulos del Proyecto

### 📘 1. Algoritmos Básicos (`algoritmos_basicos/`)

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

> Para más detalles, revisar el [README interno](algoritmos_basicos/README.md).

---

### 📗 2. Estructuras de Control y Funciones (`estructuras_de_control_funciones/`)

**25 ejercicios** organizados en 5 secciones temáticas para practicar las estructuras fundamentales de Python.

**Sección 1 — Variables y Entrada/Salida (`1.x`)**
- Manejo de tipos de datos: `str`, `int`, `float`
- Solicitud y presentación de datos al usuario
- Formateo de salida con f-strings

**Sección 2 — Estructuras Condicionales (`2.x`)**
- Uso de `if`, `elif`, `else` y `match`
- Clasificación por rangos (edades, categorías)
- Toma de decisiones con operadores lógicos y de comparación

**Sección 3 — Ciclos (`3.x`)**
- Bucles `for` y `while`
- Iteración sobre rangos y secuencias
- Control de flujo con `break` y `continue`

**Sección 4 — Listas y Estructuras de Datos (`4.x`)**
- Creación y manipulación de listas
- Operaciones CRUD sobre colecciones
- Uso de `enumerate`, búsqueda y ordenamiento

**Sección 5 — Funciones y Recursión (`5.x`)**
- Definición y llamado de funciones
- Parámetros, retorno de valores y scope
- Recursión aplicada (ej: cálculo de factorial)

---

### 📙 3. Mini Taller Integrador (`mini_taller_integrador/`)

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

- Python 3.x o superior
- `colorama` (requerido solo para `algoritmos_basicos/`)

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
cd algoritmos_basicos
python index.py

# Taller 1 - Ejecutar un algoritmo individual
python a1.py

# Taller 2 - Ejecutar un ejercicio específico
cd estructuras_de_control_funciones
python 1.1.py

# Mini Taller - Sistema de gestión de biblioteca
cd mini_taller_integrador
python gestion_biblioteca.py
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** — Lenguaje de programación principal
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
