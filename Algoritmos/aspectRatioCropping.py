import math

def convert_to_16_9_aspect_ratio(X, Y):
    # Calcular el nuevo ancho (X) manteniendo la altura (Y) constante
    new_X = Y * (16 / 9)

    # Redondear hacia arriba al entero más cercano
    new_X = math.ceil(new_X)

    return new_X, Y

# Ejemplo de uso: convertimos 1440x1080 (4:3) a una resolución de 16:9
result = convert_to_16_9_aspect_ratio(1440, 1080)
print(result)