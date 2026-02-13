# 🐍 Taller 1 - Algoritmos Python

[![Python Version](https://img.shields.io/badge/Python-3.14.3-blue.svg)](https://www.python.org/downloads/)
[![Colorama](https://img.shields.io/badge/Colorama-Latest-green.svg)](https://pypi.org/project/colorama/)

Colección de 25 algoritmos básicos en Python diseñados para practicar conceptos fundamentales de programación, incluyendo entrada/salida de datos, operaciones matemáticas, estructuras condicionales y manejo de errores.

**Desarrollado por:** Oliver Nieto

---

## 📋 Descripción

Este proyecto contiene 25 ejercicios prácticos de programación en Python que cubren temas esenciales para principiantes, desde operaciones matemáticas básicas hasta cálculos más complejos como intereses compuestos, gestión de inventarios y sistemas de comisiones.

Cada algoritmo incluye:
- ✅ Validación de entrada de datos
- ✅ Manejo de excepciones
- ✅ Interfaz de usuario colorida con `colorama`
- ✅ Comentarios descriptivos
- ✅ Buenas prácticas de programación

---

## 🚀 Características

- **Menú interactivo**: Sistema de navegación principal que lista todos los algoritmos con sus descripciones
- **Interfaz colorida**: Uso de `colorama` para mejorar la experiencia visual del usuario
- **Ejecución independiente**: Cada algoritmo puede ejecutarse de forma individual o desde el menú principal
- **Manejo de errores robusto**: Validación de entrada y mensajes de error informativos
- **Código limpio**: Documentación clara y estructura organizada

---

## 📦 Requisitos Previos

- **Python**: 3.14.3 o superior
- **Colorama**: Para la colorización de texto en terminal

---

## 🔧 Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/OliverN77/Python.git
cd Python
```

2. **Instalar dependencias**:
```bash
pip install colorama
```

---

## 💻 Uso

### Ejecutar el menú principal

```bash
python index.py
```

El menú mostrará los 25 algoritmos disponibles. Simplemente ingresa el número del algoritmo que deseas ejecutar.

### Ejecutar un algoritmo individual

```bash
python a1.py   # Ejecuta el algoritmo 1
python a15.py  # Ejecuta el algoritmo 15
```

---

## 📚 Lista de Algoritmos

### 🔢 Operaciones Matemáticas Básicas

1. **Cálculo de suma y promedio**: Solicitar al usuario tres números enteros. Calcular y mostrar la suma total y el promedio de los números ingresados.

2. **Área de un rectángulo**: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.

3. **Conversión de temperatura**: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.

### 💰 Cálculos de Salario y Comisiones

4. **Salario semanal**: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.

5. **Salario con horas extra**: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.

11. **Comisión por ventas**: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.

12. **Comisión escalonada**: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.

### 🛒 Ventas y Descuentos

6. **Total de una venta**: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.

7. **Venta con descuento fijo**: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar.

8. **Venta con descuento por porcentaje**: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.

9. **Venta con IVA**: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.

10. **Compra de varios productos**: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.

25. **Venta diaria de un almacén**: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.

### 🎓 Gestión Académica

13. **Promedio de notas**: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).

14. **Nota final ponderada**: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.

### 🔍 Comparaciones y Clasificaciones

15. **Mayor de dos números**: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

16. **Número par o impar**: Solicitar un número entero e indicar si es par o impar.

17. **Edad de una persona**: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.

18. **Clasificación por edad**: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.

### 💵 Finanzas y Conversiones

19. **Conversión de moneda**: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.

20. **Cálculo de intereses simples**: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.

21. **Cálculo de intereses compuestos**: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.

### 📦 Logística y Servicios

22. **Control de inventario**: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.

23. **Costo de envío**: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.

24. **Factura de servicios públicos**: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.

---

## 📁 Estructura del Proyecto

```
Python/
│
├── index.py          # Menú principal interactivo
├── a1.py             # Algoritmo 1: Cálculo de suma y promedio
├── a2.py             # Algoritmo 2: Área de un rectángulo
├── a3.py             # Algoritmo 3: Conversión de temperatura
├── ...               # Algoritmos 4-24
├── a25.py            # Algoritmo 25: Venta diaria de un almacén
└── README.md         # Este archivo
```

---

## 🎨 Ejemplo de Uso

Al ejecutar el menú principal (`index.py`), verás una interfaz colorida como esta:

```
========================================
Taller 1 - Algoritmos Python
By Oliver Nieto
Menú principal
========================================
1. Cálculo de suma y promedio: Solicitar al usuario...
2. Área de un rectángulo: Solicitar la base y la altura...
3. Conversión de temperatura: Solicitar una temperatura...
...
25. Venta diaria de un almacén: Solicitar el número de ventas...
0. Salir

Seleccione una opción:
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.14.3**: Lenguaje de programación principal
- **Colorama**: Librería para colorización de texto en terminal
- **Try-Except**: Manejo robusto de excepciones
- **f-strings**: Formateo moderno de cadenas

---

## 📝 Notas Adicionales

- Todos los algoritmos incluyen validación de entrada para prevenir errores de tipo
- Los valores monetarios están configurados para pesos colombianos (COP)
- Los cálculos de impuestos utilizan la tasa de IVA del 19% (Colombia)
- Cada archivo puede ejecutarse de forma independiente con `if __name__ == "__main__"`

---

## 👨‍💻 Autor

**Oliver Nieto**

---

## 📄 Licencia

Este proyecto está disponible para fines educativos y de aprendizaje.

---

## 🤝 Contribuciones

Las contribuciones, issues y solicitudes de características son bienvenidas. Siéntete libre de revisar la página de issues si deseas contribuir.

---

## ⭐ ¿Te gustó el proyecto?

Si este proyecto te fue útil, considera darle una estrella ⭐ en GitHub.

---

**¡Feliz codificación! 🚀**
