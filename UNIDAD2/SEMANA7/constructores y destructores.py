import threading
import time
import random # random se usa para simular variabilidad en los tiempos de descarga de los archivos.

def download_file(file_id):
    print(f"Iniciando la descarga del archivo {file_id}")
    download_time = random.randint(6, 12)
    time.sleep(download_time)
    print(f"Descarga del archivo {file_id} completada en {download_time} segundos")

def main():
    threads = []
    num_files = 5  # Número de archivos a descargar

    for i in range(num_files):
        thread = threading.Thread(target=download_file, args=(i,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    print("Todas las descargas han terminado.")

if __name__ == "__main__":
    main()
