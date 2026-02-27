# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.

categoria = input("Ingrese su categoría (A, B, C): ").upper()

monto_compra = float(input("Ingrese el monto de compra: "))
descuento = 0
match categoria:
    case "A":
        descuento = 0.20
    case "B":
        descuento = 0.15
    case "C":
        descuento = 0.10
        
monto_descuento = monto_compra * descuento
monto_final = monto_compra - monto_descuento
print(f"Categoría: {categoria}")
print(f"Monto de compra: ${monto_compra}")
print(f"Monto ahorrado: ${monto_descuento}")
print(f"Monto final a pagar: ${monto_final}")