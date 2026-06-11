# ============================
# SISTEMA DE GESTION DE VENTAS
# ============================

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.15
    elif subtotal >= 50000:
        return subtotal * 0.10
    else:
        return 0

def calcular_iva(monto):
    return monto * 0.19

def calcular_total(subtotal, descuento, iva):
    return subtotal - descuento + iva

def mostrar_resumen(producto, precio, cantidad, subtotal, descuento, iva, total):
    print("\n==== RESUMEN DE COMPRA ====")
    print(f"Producto: {producto}")
    print(f"Precio: ${precio:.0f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.0f}")
    print(f"Descuento: ${descuento:.0f}")
    print(f"IVA: ${iva:.0f}")
    print(f"Total: ${total:.0f}")

# Variable para acumular ventas
ventas_acumuladas = 0

while True:
    print("\n==== MENU ====")
    print("1. Registrar venta")
    print("2. Mostrar total de ventas acumuladas")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            producto = input("Ingrese nombre del producto: ")

            precio = float(input("Ingrese precio unitario: "))
            cantidad = int(input("Ingrese cantidad: "))

            subtotal = calcular_subtotal(precio, cantidad)
            descuento = calcular_descuento(subtotal)

            # IVA calculado sobre el subtotal con descuento
            iva = calcular_iva(subtotal - descuento)

            total = calcular_total(subtotal, descuento, iva)

            ventas_acumuladas += total

            mostrar_resumen(
                producto,
                precio,
                cantidad,
                subtotal,
                descuento,
                iva,
                total
            )

        elif opcion == 2:
            print(f"\nTotal de ventas acumuladas: ${ventas_acumuladas:.0f}")

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Ingrese una opción válida.")

    except ValueError:
        print("Error: Ingrese datos numéricos válidos.") 
                        