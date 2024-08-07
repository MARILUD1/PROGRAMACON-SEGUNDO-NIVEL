import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta. MOstrar en codigo que contiene el arhivo
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        print("mensaje")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = { # los archivos con su respectivo codigo

        '1': 'UNIDAD 1/SEMANA2/1.1 abstraccion.py', # Ruta del Archivos con el respectivo codigo en orden jerarjico.
        '2': 'UNIDAD 1/SEMANA2/1.2 encapsulacion.py',
        '3': 'UNIDAD 1/SEMANA2/1.3 polimorfismo.py',
        '4': 'UNIDAD 1/SEMANA2/1.4 tecnica_herencia.py',
        '5': 'UNIDAD 1/SEMANA 3/1.0 PROGRAMACION_OO.py',
        '6': 'UNIDAD 1/SEMANA 3/1. 1 TEMPERATURA_PROM.py',
        '7': 'UNIDAD 1/SEMANA4/1. 0 camioneta TOYOTA.py',
        '8': 'UNIDAD 1/SEMANA4/1.1 ej_del_docente.py',
        '9': 'UNIDAD2/SEMANA 5/1.0 tipos_de_datos_identificadores.py',
        '10': 'UNIDAD2/SEMANA_6/1.0 metodo_de_encapsulado.py',
        '11': 'UNIDAD2/SEMANA_6/1.1 metodo_herencia.py',
        '12': 'UNIDAD2/SEMANA_6/1.2 metodo_polimorfismo.py',
        '13': 'UNIDAD2/SEMANA7/1.1 constructores y destructores.py',

    }

    while True:
        print("\nMenu Principal - Dashboard")# Inicia un bucle infinito para mostrar el menú repetidamente hasta que el usuario decida salir.
        # Imprime las opciones del menú principal o padre
        for key in opciones:#Recorre las claves del diccionario 'opciones'
            print(f"{key} - {opciones[key]}")#Muestra cada opción del menú en el formato con su identificador y su valor
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")# ingresar por consola para consultar
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto Es la ubicación de un archivo o directorio
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script) # en caso de ser correcto
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")# Cuando el archivo no existe


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
