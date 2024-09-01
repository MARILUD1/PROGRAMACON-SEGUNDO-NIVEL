# Clase que referente a un libro
class Libro:
    def __init__(self, autor, titulo, categoria, isbn):
        self.autor_titulo = (autor, titulo)  # Tupla inmutable para autor y título. NO se puede cambiar
        self.categoria = categoria
        self.isbn = isbn # identificacion unica  del libro

    def __str__(self):
        return f"{self.autor_titulo[1]} por {self.autor_titulo[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase que representa al cliente o usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados al usurio : {len(self.libros_prestados)}"

# Clase se refiere a la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Tecnica Diccionario es la  ISBN clave y objeto Libro es el  valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    # Añadir libro
    def añadir_libro(self, autor, titulo, categoria, isbn):
        if isbn not in self.libros_disponibles:
            libro = Libro(autor, titulo, categoria, isbn)
            self.libros_disponibles[isbn] = libro
            print(f"Libro '{titulo}' libro añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} ya esta registrado en la biblioteca.")




    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.autor_titulo[1]}' ha fue eliminado de la biblioteca.")
        else:
            print(f"No se encontró este libro con ISBN {isbn}.")

    # Registrar usuario
    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = usuario
            self.usuarios_registrados.add(id_usuario)
            print(f"Usuario '{nombre}' registrado con éxito.")
        else:
            print(f"El ID de usuario {id_usuario} ya está registrado.")

    # Dar de baja usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.autor_titulo[1]}' prestado a {usuario.nombre}.")
        else:
            print(f"Operación fallida. Verifica si el libro o el usuario existen.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)
            if libro:
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.autor_titulo[1]}' libro devuelto a la biblioteca.")
            else:
                print(f"Este usuario no tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"No encontrado el usuario con ID {id_usuario}.")

    # Buscar libro por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        if criterio == "autor":
            encontrados = [libro for libro in self.libros_disponibles.values() if libro.autor_titulo[0] == valor]
        elif criterio == "titulo":
            encontrados = [libro for libro in self.libros_disponibles.values() if libro.autor_titulo[1] == valor]
        elif criterio == "categoria":
            encontrados = [libro for libro in self.libros_disponibles.values() if libro.categoria == valor]
        else:
            print(f"Criterio '{criterio}' no válido.")
            return

        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros por {criterio} '{valor}'.")

    # Listar libros prestados de un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")


# Función principal para interactuar con la biblioteca
def ejecutar_sistema_biblioteca():
    biblioteca = Biblioteca()

    while True:
        print("\n----- Menú de Biblioteca -----")
        print("1. Añada el libro")
        print("2. Quite el libro")
        print("3. Registre el usuario")
        print("4. Dar de  baja usuario")
        print("5. Preste el libro")
        print("6. Devolva el libro")
        print("7. Busque el  libro")
        print("8. Listar libros prestados de un usuario")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            autor = input("Introduce el autor del libro: ")
            titulo = input("Introduce el título del libro: ")
            categoria = input("Introduce la categoría del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            biblioteca.añadir_libro(autor, titulo, categoria, isbn)

        elif opcion == '2':
            isbn = input("Introduce el ISBN del libro que deseas quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':
            nombre = input("Introduce el nombre del usuario: ")
            id_usuario = input("Introduce el ID del usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == '4':
            id_usuario = input("Introduce el ID del usuario que deseas dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5':
            id_usuario = input("Introduce el ID del usuario: ")
            isbn = input("Introduce el ISBN del libro que deseas prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6':
            id_usuario = input("Introduce el ID del usuario: ")
            isbn = input("Introduce el ISBN del libro que deseas devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7':
            criterio = input("¿Deseas buscar por título, autor o categoría?: ")
            valor = input(f"Introduce el valor para {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == '8':
            id_usuario = input("Introduce el ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '9':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciar el sistema
if __name__ == "__main__":
    ejecutar_sistema_biblioteca()
