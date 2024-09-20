import math

def litres_drunk(hours):
    # Multiplicar las horas por 0.5 para obtener la cantidad de litros
    litres = hours * 0.5
    # Redondear hacia abajo usando math.floor() para obtener el valor más pequeño entero
    return math.floor(litres)

# Casos de prueba
print(litres_drunk(3))    # Debería devolver 1 litro
print(litres_drunk(6.7))  # Debería devolver 3 litros
print(litres_drunk(11.8)) # Debería devolver 5 litros
