class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
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
        self.productos = []
        self.cargar_Inventario()
    def cargar_Inventario(self):
        with open("Inventario_mejorado.txt", "r") as file:
            for line in file:
                id_producto, nombre, cantidad, precio = line.split(",")

                producto = Producto(id_producto, nombre, cantidad, precio)
                self.productos.append(producto)
    def guardar_Inventario(self):
        with open("Inventario_mejorado.txt", "a") as file:
            for producto in self.productos:
                file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio},")




    def añadir_producto(self, producto):
        # Verificar si el ID del producto es único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_Inventario()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Buscar y eliminar el producto por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_Inventario()
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=int, precio=float):
        # Buscar y actualizar el producto por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not int:
                    p.set_cantidad(cantidad)
                if precio is not float:
                    p.set_precio(precio)
                    self.guardar_Inventario()
                print("Producto actualizado correctamente.")
                return # mostrar en pantalla
        print("Error: Producto agotado.")

    def buscar_producto_por_nombre(self, nombre):
        # Buscar productos por nombre (o parte del nombre)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                self.guardar_Inventario()
                print(p)
        else:

            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        # Mostrar todos los productos en el inventario
        if not self.productos:
            print()
        else:
            for p in self.productos:
                print(p)


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
        try:
            # Intenta ejecutar este bloque de código que puede lanzar excepciones
            resultado = 10 / 0  # Esto provocará un ZeroDivisionError
            # resultado = int("no es un número")  # Descomenta para probar ValueError
        except ZeroDivisionError:
            print("Error: División por cero.")
        except ValueError:
            print("Error: Valor no válido.")
        except:
            # Captura cualquier otra excepción no capturada por los except anteriores
            print("Error desconocido.")

        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)



        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    gestionar_inventario()



