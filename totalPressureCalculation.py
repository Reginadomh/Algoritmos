def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Constantes
    R = 0.082  # constante de gases en dm^3⋅atm⋅K^−1⋅mol^−1

    # Convertir la temperatura de Celsius a Kelvin
    T_kelvin = T + 273.15

    # Calcular la presión total usando la fórmula dada
    P_total = (m1 / M1 + m2 / M2) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
M1 = 28.97  # Masa molar del primer gas en g/mol
M2 = 44.01  # Masa molar del segundo gas en g/mol
m1 = 10  # Masa del primer gas en gramos
m2 = 20  # Masa del segundo gas en gramos
V = 5  # Volumen del recipiente en dm^3
T = 25  # Temperatura en Celsius

P_total = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f'Presión Total: {P_total:.2f} atm')
