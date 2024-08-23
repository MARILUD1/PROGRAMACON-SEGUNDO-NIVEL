# Usando 'with' para abrir el archivo en modo escritura (creándolo si no existe).
# Escribe en él y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'w') as archivo:
    archivo.write('Escribe tu archivo.')  # Escribe en el archivo

# Usando 'with' para abrir el archivo en modo añadir.
# Añade una nueva línea y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'a') as archivo:
    archivo.write('\nProgramacion Orirntada a Objetos .')
    archivo.write('\nsemana 10.') #Añade nueva línea de texto
    archivo.write('\nManipulacion de archivos y manejo de exepciones.')
# Usando 'with' para abrir el archivo en modo lectura.
with open('ejemplo_escritura.txt', 'r') as archivo:
    print(archivo.read())  # Imprime el contenido del archivo