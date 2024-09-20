def extrapolar_ppg(ppg, mpg):
    # Si los minutos jugados son 0, se devuelve 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Calcular los puntos extrapolados para 48 minutos
    ppg_extrapolado = (ppg / mpg) * 48

    # Redondear al decimal más cercano
    ppg_extrapolado_redondeado = round(ppg_extrapolado, 1)

    return ppg_extrapolado_redondeado


# Ejemplo de uso
ppg = 15.5  # puntos por juego
mpg = 30  # minutos jugados por juego

resultado = extrapolar_ppg(ppg, mpg)
print(f'PPG extrapolado para 48 minutos: {resultado:.1f}')
