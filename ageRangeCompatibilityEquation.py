import math


def rango_edad(edad):
    if edad > 14:
        min_edad = (edad / 2) + 7
        max_edad = (edad - 7) * 2
    else:
        min_edad = edad - 0.10 * edad
        max_edad = edad + 0.10 * edad

    # Redondear hacia abajo
    min_edad = math.floor(min_edad)
    max_edad = math.floor(max_edad)

    return f'{min_edad}-{max_edad}'


# Ejemplo de uso
edad = 25  # edad de la persona

resultado = rango_edad(edad)
print(f'Rango de edad: {resultado}')
