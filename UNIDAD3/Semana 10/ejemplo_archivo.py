
 # Usando 'with' para abrir el archivo en modo lectura.
archivo = open('ejm_lectura.txt', 'r')
print(archivo.read())  # Imprime el contenido del archivo
archivo.close()