def calcular_temperatura_promedio_semanal(datos, ciudad):
    num_semanas = len(datos)
    suma_temperatura = 0
    num_registros = 0

    # Recorrer cada semana y sumar las temperaturas de la ciudad especificada
    for semana in range(num_semanas):
        for registro in datos[semana]:
            if registro[0].lower() == ciudad.lower():
                suma_temperatura += registro[2]
                num_registros += 1

    if num_registros == 0:
        raise ValueError(f"No se encontraron registros para la ciudad '{ciudad}' en los datos proporcionados.")

    promedio_semanal = suma_temperatura / num_semanas
    return promedio_semanal

# Datos de temperaturas por ciudades y semanas
dimension_temperaturas = [
    [   # Semana 1
        ["Quito", "temperatura", 17],
        ["Guayaquil", "temperatura", 18],
        ["Cuenca", "temperatura", 20],
        ["Machala", "temperatura", 26],
        ["Riobamba", "temperatura", 26],
        ["Ambato", "temperatura", 19],
        ["Loja", "temperatura", 23]
    ],
    [   # Semana 2
        ["Quito", "temperatura", 19],
        ["Guayaquil", "temperatura", 26],
        ["Cuenca", "temperatura", 18],
        ["Machala", "temperatura", 29],
        ["Riobamba", "temperatura", 18],
        ["Ambato", "temperatura", 122],
        ["Loja", "temperatura", 19]
    ],
    [   # Semana 3
        ["Quito", "temperatura", 20],
        ["Guayaquil", "temperatura", 25],
        ["Cuenca", "temperatura", 19],
        ["Machala", "temperatura", 28],
        ["Riobamba", "temperatura", 22],
        ["Ambato", "temperatura", 17],
        ["Loja", "temperatura", 18]
    ]
]

# Solicitar entrada al usuario
ciudad = input("Ingrese el nombre de la ciudad (Quito, Guayaquil, Cuenca, Machala, Riobamba, Ambato, Loja): ")

try:
    promedio_semanal = calcular_temperatura_promedio_semanal(dimension_temperaturas, ciudad)
    print(f"El promedio de temperatura semanal para la ciudad de {ciudad} es: {promedio_semanal:.2f}")
except ValueError as e:
    print(f"Error: {e}")
