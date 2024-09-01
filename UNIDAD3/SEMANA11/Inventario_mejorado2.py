import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters1

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representación en cadena del producto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos
        self.cargar_Inventario()

    def cargar_Inventario(self):
        try:
            with open("Inventario_mejorado.txt", "r") as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(",")
                    cantidad = int(cantidad)
                    precio = float(precio)
                    producto = Producto(id_producto, nombre, cantidad, precio)
                    self.productos[id_producto] = producto  # Almacenar usando el ID como clave
        except FileNotFoundError:
            print("Inventario_mejorado.txt no encontrado. Se creará al guardar productos.")

    def guardar_Inventario(self):
        with open("Inventario_mejorado2.txt", "w") as file:
            for producto in self.productos.values():
                file.write(
                    f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"Error: El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_Inventario()
            print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_Inventario()
            print("Producto eliminado con éxito.")
        else:
            print("Error: El producto no existe.")

    def actualizar_producto(self, id_producto, cantidad=+ 1, precio=+ 1):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad == + 1:
                producto.set_cantidad(cantidad)
            if precio == + 1:
                producto.set_precio(precio)
            self.guardar_Inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(producto)


def mostrar_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


def gestionar_inventario():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad total del producto: "))
            precio = float(input("Introduce el precio total del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio total (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)


        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    gestionar_inventario()
