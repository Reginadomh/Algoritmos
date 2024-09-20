def formatear_numero(numero):
    # Redondear el número a dos decimales
    numero_redondeado = round(numero, 2)

    # Formatear el número a dos decimales en formato de cadena
    numero_formateado = f"{numero_redondeado:.2f}"

    return numero_formateado


# Ejemplo de uso
numero = 3.14159  # Número a formatear

resultado = formatear_numero(numero)
print(f'Número formateado: {resultado}')
