
# Registrar productos de una tienda

def main():
    # 1. Creación de la colección de datos (Lista vacía)
    inventario = []

    print("=== SISTEMA DE GESTIÓN DE TIENDA ===")

    # 2. Funcionalidad para INSERTAR / AGREGAR datos
    print("AGREGANDO PRODUCTOS AL INVENTARIO")
    inventario.append({"nombre": "Arroz (1 kg)", "precio": 1.25})
    inventario.append({"nombre": "Leche (1 L)", "precio": 0.90})
    inventario.append({"nombre": "Aceite (1 L)", "precio": 2.50})
    print("Se han registrado 3 productos con éxito.")

    # 3. MOSTRAR de forma clara la información almacenada
    print("INVENTARIO ACTUAL DE LA TIENDA")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f}")

    # 4. OPERACIÓN ADICIONAL 1: Búsqueda de un producto
    print("BUSCANDO UN PRODUCTO")
    busqueda = "Leche (1 L)"
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == busqueda.lower():
            print(f"Producto encontrado: {producto['nombre']} -> Precio: ${producto['precio']:.2f}")
            encontrado = True
            break
    if not encontrado:
        print(f"El producto '{busqueda}' no está disponible.")

    # 4. OPERACIÓN ADICIONAL 2: Eliminar un producto
    print("ELIMINANDO UN PRODUCTO")
    producto_a_eliminar = "Arroz (1 kg)"
    inventario = [p for p in inventario if p["nombre"] != producto_a_eliminar]
    print(f"Producto '{producto_a_eliminar}' eliminado del inventario.")

    # 5. MOSTRAR la lista actualizada tras la eliminación
    print("INVENTARIO ACTUALIZADO")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f}")

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()
    

